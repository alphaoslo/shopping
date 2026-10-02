import os
import uuid

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    current_app,
)

from werkzeug.utils import secure_filename

from models import db, Product, Category, Brand
from admin.products import products_bp
from utils.auth import admin_required



@products_bp.route("/")
@admin_required
def index():

    products = Product.query.order_by(Product.id.desc()).all()

    return render_template(
        "admin/products/list.html",
        products=products,
    )

@products_bp.route("/create", methods=["GET", "POST"])
@admin_required
def create():
    """
    Create a new product.
    """

    categories = Category.query.order_by(Category.name).all()

    brands = Brand.query.order_by(Brand.name).all()

    if request.method == "POST":

        # ==========================================
        # FORM DATA
        # ==========================================

        name = request.form.get("name")
        sku = request.form.get("sku")

        category_id = int(request.form.get("category_id"))
        brand_id = int(request.form.get("brand_id"))

        original_price = float(
            request.form.get("original_price")
        )

        price = float(
            request.form.get("price")
        )

        discount = float(
            request.form.get("discount") or 0
        )

        stock = int(
            request.form.get("stock")
        )

        description = request.form.get("description")

        is_active = "is_active" in request.form
        is_featured = "is_featured" in request.form
        is_best_seller = "is_best_seller" in request.form

        # ==========================================
        # PRODUCT IMAGE
        # ==========================================

        image_file = request.files.get("image")

        image_filename = None

        if image_file and image_file.filename:

            original_filename = secure_filename(
                image_file.filename
            )

            extension = os.path.splitext(
                original_filename
            )[1].lower()

            allowed_extensions = current_app.config[
                "ALLOWED_IMAGE_EXTENSIONS"
            ]

            if extension.lstrip(".") not in allowed_extensions:

                flash(
                    "Invalid image format. Please upload JPG, PNG or WEBP.",
                    "danger",
                )

                return render_template(
                    "admin/products/create.html",
                    categories=categories,
                    brands=brands,
                )

            # Generate unique filename
            image_filename = (
                f"{uuid.uuid4().hex}{extension}"
            )

            upload_folder = current_app.config[
                "PRODUCT_UPLOAD_FOLDER"
            ]

            # Make sure upload directory exists
            os.makedirs(
                upload_folder,
                exist_ok=True,
            )

            image_path = os.path.join(
                upload_folder,
                image_filename,
            )

            image_file.save(image_path)

        # ==========================================
        # CREATE PRODUCT
        # ==========================================

        new_product = Product(

            name=name,

            sku=sku,

            description=description,

            price=price,

            original_price=original_price,

            discount=discount,

            stock=stock,

            image=image_filename,

            is_active=is_active,

            is_featured=is_featured,

            is_best_seller=is_best_seller,

            category_id=category_id,

            brand_id=brand_id,
        )

        db.session.add(new_product)

        db.session.commit()

        flash(
            "Product added successfully!",
            "success",
        )

        return redirect(
            url_for("admin.products.index")
        )

    # ==========================================
    # GET REQUEST
    # ==========================================

    return render_template(
        "admin/products/create.html",
        categories=categories,
        brands=brands,
    )

@products_bp.route("/<int:product_id>/edit", methods=["GET", "POST"])
@admin_required
def edit(product_id):
    """
    Edit Product
    """

    product = Product.query.get_or_404(product_id)

    categories = Category.query.order_by(Category.name).all()
    brands = Brand.query.order_by(Brand.name).all()

    if request.method == "POST":

        # ==========================================
        # PRODUCT INFORMATION
        # ==========================================

        product.name = request.form.get("name")

        # Preserve existing SKU if the form does not provide one
        sku = request.form.get("sku")

        if sku and sku.strip():
            sku = sku.strip()

            # Check whether another product already uses this SKU
            existing_product = Product.query.filter(
                Product.sku == sku,
                Product.id != product.id
            ).first()

            if existing_product:
                flash(
                    "This SKU is already used by another product.",
                    "danger",
                )

                return render_template(
                    "admin/products/edit.html",
                    product=product,
                    categories=categories,
                    brands=brands,
                )

            product.sku = sku

        # ==========================================
        # CATEGORY & BRAND
        # ==========================================

        category_id = request.form.get("category_id")
        brand_id = request.form.get("brand_id")

        if category_id:
            product.category_id = int(category_id)

        if brand_id:
            product.brand_id = int(brand_id)

        # ==========================================
        # PRICING
        # ==========================================

        original_price = request.form.get("original_price")
        price = request.form.get("price")
        discount = request.form.get("discount")

        if original_price:
            product.original_price = float(original_price)

        if price:
            product.price = float(price)

        product.discount = float(discount or 0)

        # ==========================================
        # INVENTORY
        # ==========================================

        stock = request.form.get("stock")

        if stock:
            product.stock = int(stock)

        # ==========================================
        # DESCRIPTION
        # ==========================================

        product.description = request.form.get("description")

        # ==========================================
        # STATUS
        # ==========================================

        product.is_active = "is_active" in request.form

        product.is_featured = "is_featured" in request.form

        product.is_best_seller = "is_best_seller" in request.form

        # ==========================================
        # IMAGE
        # ==========================================

        image_file = request.files.get("image")

        if image_file and image_file.filename:

            from werkzeug.utils import secure_filename
            import os
            import uuid

            filename = secure_filename(image_file.filename)

            extension = os.path.splitext(filename)[1].lower()

            new_filename = f"{uuid.uuid4().hex}{extension}"

            upload_folder = os.path.join(
                "static",
                "uploads",
                "products",
            )

            os.makedirs(
                upload_folder,
                exist_ok=True,
            )

            image_file.save(
                os.path.join(
                    upload_folder,
                    new_filename,
                )
            )

            product.image = new_filename

        # ==========================================
        # SAVE
        # ==========================================

        db.session.commit()

        flash(
            "Product updated successfully!",
            "success",
        )

        return redirect(
            url_for("admin.products.index")
        )

    # ==========================================
    # DISPLAY EDIT PAGE
    # ==========================================

    return render_template(
        "admin/products/edit.html",
        product=product,
        categories=categories,
        brands=brands,
    )