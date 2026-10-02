from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

from models import db, Product
from admin.inventory import inventory_bp
from admin.inventory.services import InventoryService
from utils.auth import admin_required


@inventory_bp.route("/")
@admin_required
def index():
    products = InventoryService.get_all_products()
    low_stock = InventoryService.get_low_stock()
    out_of_stock = InventoryService.get_out_of_stock()
    return render_template(
        "admin/inventory/list.html",
        products=products,
        low_stock=low_stock,
        out_of_stock=out_of_stock,
    )


@inventory_bp.route("/<int:product_id>/update", methods=["POST"])
@admin_required
def update_stock(product_id):
    quantity = request.form.get("stock")
    product, message = InventoryService.update_stock(product_id, quantity)
    flash(message, "success" if product else "danger")
    return redirect(url_for("admin.inventory.index"))
