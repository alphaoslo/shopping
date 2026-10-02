from flask import render_template
from sqlalchemy import func

from models import db, Order, OrderItem, Product, Category, Brand
from admin.reports import reports_bp
from utils.auth import admin_required


@reports_bp.route("/")
@admin_required
def index():
    total_orders = Order.query.count()
    total_revenue = db.session.query(
        func.coalesce(func.sum(Order.total_amount), 0)
    ).filter(Order.status != "Cancelled").scalar()

    pending_orders = Order.query.filter_by(status="Pending").count()
    cancelled_orders = Order.query.filter_by(status="Cancelled").count()
    delivered_orders = Order.query.filter_by(status="Delivered").count()

    # Top selling products
    top_products = (
        db.session.query(
            Product.name,
            func.sum(OrderItem.quantity).label("total_sold"),
            func.sum(OrderItem.subtotal).label("revenue"),
        )
        .join(OrderItem, OrderItem.product_id == Product.id)
        .group_by(Product.id)
        .order_by(func.sum(OrderItem.quantity).desc())
        .limit(5)
        .all()
    )

    # Category sales
    category_sales = (
        db.session.query(
            Category.name,
            func.sum(OrderItem.quantity).label("total_sold"),
            func.sum(OrderItem.subtotal).label("revenue"),
        )
        .join(Product, Product.category_id == Category.id)
        .join(OrderItem, OrderItem.product_id == Product.id)
        .group_by(Category.id)
        .order_by(func.sum(OrderItem.subtotal).desc())
        .all()
    )

    # Brand sales
    brand_sales = (
        db.session.query(
            Brand.name,
            func.sum(OrderItem.quantity).label("total_sold"),
            func.sum(OrderItem.subtotal).label("revenue"),
        )
        .join(Product, Product.brand_id == Brand.id)
        .join(OrderItem, OrderItem.product_id == Product.id)
        .group_by(Brand.id)
        .order_by(func.sum(OrderItem.subtotal).desc())
        .all()
    )

    # Inventory status
    total_products = Product.query.count()
    low_stock = Product.query.filter(Product.stock <= 5, Product.stock > 0).count()
    out_of_stock = Product.query.filter(Product.stock <= 0).count()

    return render_template(
        "admin/reports/index.html",
        total_orders=total_orders,
        total_revenue=total_revenue,
        pending_orders=pending_orders,
        cancelled_orders=cancelled_orders,
        delivered_orders=delivered_orders,
        top_products=top_products,
        category_sales=category_sales,
        brand_sales=brand_sales,
        total_products=total_products,
        low_stock=low_stock,
        out_of_stock=out_of_stock,
    )
