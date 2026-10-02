from flask import Blueprint, render_template
from models import Product, Category, Brand
from utils.auth import admin_required   

admin_routes_bp = Blueprint(
    "admin_routes",
    __name__,
)


@admin_routes_bp.route("/dashboard")
@admin_required
def dashboard():
    """
    Admin Dashboard
    """

    total_products = Product.query.count()
    total_categories = Category.query.count()
    total_brands = Brand.query.count()

    return render_template(
        "admin/dashboard/dashboard.html",
        total_products=total_products,
        total_categories=total_categories,
        total_brands=total_brands,
    )