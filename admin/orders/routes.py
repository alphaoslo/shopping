from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

from models import Order
from admin.orders import orders_bp
from admin.orders.services import OrderService, VALID_STATUSES
from utils.auth import admin_required


@orders_bp.route("/")
@admin_required
def index():
    status = request.args.get("status", "").strip() or None
    search = request.args.get("search", "").strip() or None
    orders = OrderService.get_all(status=status, search=search)
    return render_template(
        "admin/orders/list.html",
        orders=orders,
        status=status,
        search=search,
        statuses=VALID_STATUSES,
    )


@orders_bp.route("/<int:order_id>")
@admin_required
def details(order_id):
    order = OrderService.get_by_id(order_id)
    items = OrderService.get_items(order_id)
    return render_template(
        "admin/orders/details.html",
        order=order,
        items=items,
        statuses=VALID_STATUSES,
    )


@orders_bp.route("/<int:order_id>/status", methods=["POST"])
@admin_required
def update_status(order_id):
    status = request.form.get("status")
    order, message = OrderService.update_status(order_id, status)
    flash(message, "success" if order else "danger")
    return redirect(url_for("admin.orders.details", order_id=order_id))
