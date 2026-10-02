from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import razorpay
from models.product import Product
from models.brand import Brand
from models.category import Category
from models.order import Order
from models.order_item import OrderItem
from models import db
from datetime import timedelta
from flask import current_app

def get_razorpay_client():
    """
    Returns a configured Razorpay client using the
    credentials stored in config.py.
    """
    return razorpay.Client(
        auth=(
            current_app.config["RAZORPAY_KEY_ID"],
            current_app.config["RAZORPAY_KEY_SECRET"],
        )
    )

customer_bp = Blueprint(
    "customer",
    __name__
)


@customer_bp.route("/")
def home():

    featured_products = (
        Product.query
        .filter_by(is_featured=True)
        .order_by(Product.id.asc())
        .limit(8)
        .all()
    )

    best_sellers = (
        Product.query
        .filter_by(is_best_seller=True)
        .order_by(Product.id.asc())
        .limit(8)
        .all()
    )

    brands = (
        Brand.query
        .order_by(Brand.name.asc())
        .all()
    )
    categories = (
        Category.query
        .order_by(Category.name.asc())
        .all()
    )

    return render_template(
        "customer/home.html",
        featured_products=featured_products,
        best_sellers=best_sellers,
        brands=brands,
        categories=categories
    )
@customer_bp.route("/products")
def products():

    search = request.args.get("search", "").strip()
    category_id = request.args.get("category", type=int)
    brand_id = request.args.get("brand", type=int)   # NEW
    sort = request.args.get("sort", "")
    page = request.args.get("page", 1, type=int)
    query = Product.query

    if search:
        query = query.filter(
            Product.name.ilike(f"%{search}%")
        )

    if category_id:
        query = query.filter(
            Product.category_id == category_id
        )

    if brand_id:   # NEW
        query = query.filter(
            Product.brand_id == brand_id
        )

    if sort == "price_low":
        query = query.order_by(Product.price.asc())
    elif sort == "price_high":

        query = query.order_by(Product.price.desc())
    elif sort == "rating":

        query = query.order_by(Product.rating.desc())

    elif sort == "newest":

        query = query.order_by(Product.created_at.desc())

    else:

        query = query.order_by(Product.id.asc())    
    products = query.paginate(
        page=page,
        per_page=8,
        error_out=False
)

    categories = (
        Category.query
        .order_by(Category.name.asc())
        .all()
    )

    brands = (      # NEW
        Brand.query
        .order_by(Brand.name.asc())
        .all()
    )

    return render_template(
        "customer/products.html",
        products=products,
        categories=categories,
        brands=brands,          # NEW
        search=search,
        category_id=category_id,
        brand_id=brand_id,       # NEW
        sort=sort,
        page=page
    )
@customer_bp.route("/products/<int:product_id>")
def product_details(product_id):

    product = Product.query.get_or_404(product_id)

    related_products = (
        Product.query
        .filter(
            Product.category_id == product.category_id,
            Product.id != product.id
        )
        .limit(4)
        .all()
    )

    return render_template(
        "customer/product_details.html",
        product=product,
        related_products=related_products
    )
@customer_bp.route("/cart/add/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):

    product = Product.query.get_or_404(product_id)

    quantity = int(request.form.get("quantity", 1))

    if quantity > product.stock:
        flash(
            f"Only {product.stock} item(s) available in stock.",
            "danger"
        )
        return redirect(request.referrer or url_for("customer.products"))

    cart = session.get("cart", {})

    product_id_str = str(product.id)

    current_quantity = cart.get(product_id_str, 0)

    if current_quantity + quantity > product.stock:
        flash(
            f"Only {product.stock} item(s) available in stock.",
            "danger"
        )
        return redirect(request.referrer or url_for("customer.products"))

    cart[product_id_str] = current_quantity + quantity

    session["cart"] = cart

    flash(f"{product.name} added to cart successfully!", "success")

    return redirect(request.referrer or url_for("customer.products"))
@customer_bp.route("/cart")
def cart():

    cart = session.get("cart", {})

    cart_items = []

    total = 0

    for product_id, quantity in cart.items():

        product = Product.query.get(int(product_id))

        if product:

            subtotal = product.price * quantity

            total += subtotal

            cart_items.append({
                "product": product,
                "quantity": quantity,
                "subtotal": subtotal
            })

    return render_template(
        "customer/cart.html",
        cart_items=cart_items,
        total=total
    )

@customer_bp.route("/cart/remove/<int:product_id>", methods=["POST"])
def remove_from_cart(product_id):

    cart = session.get("cart", {})

    product_id_str = str(product_id)

    if product_id_str in cart:
        del cart[product_id_str]

    session["cart"] = cart

    flash("Item removed from cart.", "danger")

    return redirect(url_for("customer.cart"))
@customer_bp.route("/cart/update/<int:product_id>", methods=["POST"])
def update_cart(product_id):

    cart = session.get("cart", {})

    product = Product.query.get_or_404(product_id)

    product_id_str = str(product_id)

    action = request.form.get("action")

    if product_id_str in cart:

        if action == "increase":

            if cart[product_id_str] < product.stock:

                cart[product_id_str] += 1
                flash("Quantity increased.", "info")

            else:

                flash(
                    f"Only {product.stock} item(s) available.",
                    "warning"
                )

        elif action == "decrease":

            if cart[product_id_str] > 1:

                cart[product_id_str] -= 1
                flash("Quantity decreased.", "warning")

            else:

                del cart[product_id_str]
                flash("Item removed from cart.", "danger")

    session["cart"] = cart

    return redirect(url_for("customer.cart"))
@customer_bp.route("/checkout")
def checkout():

    cart = session.get("cart", {})

    if not cart:

        flash("Your cart is empty.", "warning")

        return redirect(url_for("customer.products"))

    cart_items = []

    total = 0

    for product_id, quantity in cart.items():

        product = Product.query.get(int(product_id))

        if product:

            subtotal = product.price * quantity

            total += subtotal

            cart_items.append({

                "product": product,

                "quantity": quantity,

                "subtotal": subtotal

            })
    # ----------------------------------------
    # Create Razorpay Order
    # ----------------------------------------

    client = get_razorpay_client()

    razorpay_order = client.order.create({
        "amount": int(total * 100),   # Amount in paise
        "currency": "INR",
        "payment_capture": 1
    })

    return render_template(
        "customer/checkout.html",
        cart_items=cart_items,
        total=total,
        razorpay_order_id=razorpay_order["id"],
        razorpay_key=current_app.config["RAZORPAY_KEY_ID"]
    )

    return render_template(

        "customer/checkout.html",

        cart_items=cart_items,

        total=total

    )
    
def create_order_after_payment(
    customer_data,
    cart,
    razorpay_order_id,
    razorpay_payment_id
):
    """
    Creates order, order items, updates stock,
    clears cart and returns the created order.
    """

    total = 0

    # Calculate total
    for product_id, quantity in cart.items():
        product = Product.query.get(int(product_id))
        if product:
            total += product.price * quantity

    # Create Order
    order = Order(
    customer_name=customer_data["customer_name"],
    email=customer_data["email"],
    phone=customer_data["phone"],
    address=customer_data["address"],
    city=customer_data["city"],
    state=customer_data["state"],
    pincode=customer_data["pincode"],
    notes=customer_data["notes"],
    total_amount=total,

    payment_status="Paid",
    razorpay_order_id=razorpay_order_id,
    razorpay_payment_id=razorpay_payment_id,

    status="Pending"
)

    db.session.add(order)
    db.session.commit()

    # Create Order Items
    for product_id, quantity in cart.items():

        product = Product.query.get(int(product_id))

        if product:

            order_item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=quantity,
                price=product.price,
                subtotal=product.price * quantity
            )

            db.session.add(order_item)

            # Reduce stock only after payment
            product.stock -= quantity

    db.session.commit()

    session.pop("cart", None)

    return order

@customer_bp.route("/start-payment", methods=["POST"])
def start_payment():

    cart = session.get("cart", {})

    if not cart:
        flash("Your cart is empty.", "warning")
        return redirect(url_for("customer.products"))

    # ==========================
    # Customer Details
    # ==========================

    customer_name = request.form.get("customer_name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    city = request.form.get("city")
    state = request.form.get("state")
    pincode = request.form.get("pincode")
    address = request.form.get("address")
    notes = request.form.get("notes")

    # ==========================
    # Validate Stock
    # ==========================

    total = 0

    for product_id, quantity in cart.items():

        product = Product.query.get(int(product_id))

        if not product:
            flash("A product is no longer available.", "danger")
            return redirect(url_for("customer.cart"))

        if quantity > product.stock:
            flash(
                f"{product.name} has only {product.stock} item(s) left.",
                "danger"
            )
            return redirect(url_for("customer.cart"))

        total += product.price * quantity

    # ==========================
    # Save Customer Details
    # ==========================

    session["checkout_details"] = {
        "customer_name": customer_name,
        "phone": phone,
        "email": email,
        "city": city,
        "state": state,
        "pincode": pincode,
        "address": address,
        "notes": notes
    }

    # ==========================
    # Create Razorpay Order
    # ==========================

    client = get_razorpay_client()

    razorpay_order = client.order.create({
        "amount": int(total * 100),
        "currency": "INR",
        "payment_capture": 1
    })

    session["razorpay_order_id"] = razorpay_order["id"]

    return render_template(
        "customer/payment.html",
        razorpay_order_id=razorpay_order["id"],
        razorpay_key=current_app.config["RAZORPAY_KEY_ID"],
        total=total
    )

@customer_bp.route("/place-order", methods=["POST"])
def place_order():

    cart = session.get("cart", {})

    if not cart:
        flash("Your cart is empty.", "warning")
        return redirect(url_for("customer.products"))

    # ==========================
    # Customer Details
    # ==========================

    customer_name = request.form.get("customer_name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    city = request.form.get("city")
    state = request.form.get("state")
    pincode = request.form.get("pincode")
    address = request.form.get("address")
    notes = request.form.get("notes")

    # ==========================
    # Validate Product Stock
    # ==========================

    for product_id, quantity in cart.items():

        product = Product.query.get(int(product_id))

        if not product:
            flash("A product is no longer available.", "danger")
            return redirect(url_for("customer.cart"))

        if quantity > product.stock:
            flash(
                f"{product.name} has only {product.stock} item(s) left.",
                "danger"
            )
            return redirect(url_for("customer.cart"))

    # ==========================
    # Calculate Total Amount
    # ==========================

    total = 0

    for product_id, quantity in cart.items():

        product = Product.query.get(int(product_id))

        if product:
            total += product.price * quantity
    # ==========================
    # Save Customer Details
    # ==========================
 
    session["checkout_details"] = {
        "customer_name": customer_name,
        "phone": phone,
        "email": email,
        "city": city,
        "state": state,
        "pincode": pincode,
        "address": address,
        "notes": notes
    }

    # ==========================
    # Create Order
    # ==========================
    order = Order(
        customer_name=customer_name,
        email=email,
        phone=phone,
        address=address,
        city=city,
        state=state,
        pincode=pincode,
        notes=notes,
        total_amount=total
    )

    db.session.add(order)
    db.session.commit()

    # ==========================
    # Create Order Items
    # ==========================

    for product_id, quantity in cart.items():

        product = Product.query.get(int(product_id))

        if product:

            order_item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=quantity,
                price=product.price,
                subtotal=product.price * quantity
            )

            db.session.add(order_item)

    db.session.commit()

    # ==========================
    # Reduce Product Stock
    # ==========================
    for product_id, quantity in cart.items():
        product = Product.query.get(int(product_id))
        if product:
            product.stock -= quantity
    db.session.commit()

    # ==========================
    # Clear Cart
    # ==========================

    session.pop("cart", None)

    flash("Order placed successfully!", "success")

    return redirect(url_for("customer.order_success"))

@customer_bp.route("/payment/success", methods=["POST"])
def payment_success():
    try:

        client = get_razorpay_client()

        razorpay_order_id = request.form.get("razorpay_order_id")
        razorpay_payment_id = request.form.get("razorpay_payment_id")
        razorpay_signature = request.form.get("razorpay_signature")

        # ==========================
        # Verify Razorpay Signature
        # ==========================

        client.utility.verify_payment_signature({
            "razorpay_order_id": razorpay_order_id,
            "razorpay_payment_id": razorpay_payment_id,
            "razorpay_signature": razorpay_signature
        })

        # ==========================
        # Retrieve Session Data
        # ==========================

        customer_data = session.get("checkout_details")
        cart = session.get("cart", {})

        if not customer_data:
            flash("Checkout session expired.", "warning")
            return redirect(url_for("customer.checkout"))

        if not cart:
            flash("Your cart is empty.", "warning")
            return redirect(url_for("customer.products"))

        # ==========================
        # Create Order
        # ==========================

        order = create_order_after_payment(
            customer_data=customer_data,
            cart=cart,
            razorpay_order_id=razorpay_order_id,
            razorpay_payment_id=razorpay_payment_id
        )

        # ==========================
        # Clear Checkout Session
        # ==========================

        session.pop("checkout_details", None)

        flash("Payment successful! Your order has been placed.", "success")

        return redirect(url_for("customer.order_success"))

    except razorpay.errors.SignatureVerificationError:

        flash("Payment verification failed.", "danger")

        return redirect(url_for("customer.checkout"))

    except Exception as e:

        db.session.rollback()

        print(e)

        flash("Something went wrong while placing your order.", "danger")

        return redirect(url_for("customer.checkout"))
@customer_bp.route("/order-success")
def order_success():

    return render_template("customer/order_success.html")

@customer_bp.route("/orders")
def orders():

    orders = Order.query.order_by(Order.created_at.desc()).all()

    return render_template(
        "customer/orders.html",
        orders=orders,
        timedelta=timedelta
    )

@customer_bp.route("/orders/<int:order_id>")
def order_details(order_id):

    order = Order.query.get_or_404(order_id)

    order_items = OrderItem.query.filter_by(
        order_id=order.id
    ).all()

    return render_template(
        "customer/order_details.html",
        order=order,
        order_items=order_items,
        timedelta=timedelta
    )
@customer_bp.route("/buy-now/<int:product_id>", methods=["POST"])
def buy_now(product_id):

    product = Product.query.get_or_404(product_id)

    quantity = int(request.form.get("quantity", 1))

    cart = {}

    cart[str(product.id)] = quantity

    session["cart"] = cart

    return redirect(url_for("customer.checkout"))
@customer_bp.route("/orders/<int:order_id>/cancel", methods=["POST"])
def cancel_order(order_id):

    order = Order.query.get_or_404(order_id)

    if order.status not in ["Pending", "Processing"]:

        flash("This order cannot be cancelled.", "danger")
        return redirect(url_for("customer.orders"))

    try:

        # ==========================
        # Refund Razorpay Payment
        # ==========================

        if (
            order.payment_status == "Paid"
            and order.razorpay_payment_id
        ):

            client = get_razorpay_client()

            client.payment.refund(
                order.razorpay_payment_id,
                {
                    "amount": int(order.total_amount * 100)
                }
            )

            order.payment_status = "Refunded"

        # ==========================
        # Cancel Order
        # ==========================

        order.status = "Cancelled"

        # ==========================
        # Restore Stock
        # ==========================

        for item in order.items:

            item.product.stock += item.quantity

        db.session.commit()

        flash(
            "Order cancelled and refund initiated successfully.",
            "success"
        )

    except Exception as e:

        db.session.rollback()

        print(e)

        flash(
            "Unable to process refund. Order was not cancelled.",
            "danger"
        )

    return redirect(url_for("customer.orders"))