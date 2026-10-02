"""
Order Services

Business logic for Order Management.
"""

from models import db, Order, OrderItem

VALID_STATUSES = [
    "Pending",
    "Processing",
    "Shipped",
    "Delivered",
    "Cancelled",
]


class OrderService:

    @staticmethod
    def get_all(status=None, search=None):
        query = Order.query

        if status:
            query = query.filter(Order.status == status)

        if search:
            query = query.filter(
                db.or_(
                    Order.customer_name.ilike(f"%{search}%"),
                    Order.email.ilike(f"%{search}%"),
                    Order.phone.ilike(f"%{search}%"),
                )
            )

        return query.order_by(Order.created_at.desc()).all()

    @staticmethod
    def get_by_id(order_id):
        return Order.query.get_or_404(order_id)

    @staticmethod
    def get_items(order_id):
        return OrderItem.query.filter_by(order_id=order_id).all()

    @staticmethod
    def update_status(order_id, status):
        order = Order.query.get_or_404(order_id)

        if status not in VALID_STATUSES:
            return None, "Invalid status."

        order.status = status
        db.session.commit()
        return order, "Order status updated."
