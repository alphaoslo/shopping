from datetime import datetime

from models import db


class Order(db.Model):

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)

    customer_name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), nullable=False)

    phone = db.Column(db.String(20), nullable=False)

    address = db.Column(db.Text, nullable=False)

    city = db.Column(db.String(100), nullable=False)

    state = db.Column(db.String(100), nullable=False)

    pincode = db.Column(db.String(10), nullable=False)

    notes = db.Column(db.Text)

    total_amount = db.Column(db.Float, nullable=False)

    status = db.Column(
        db.String(30),
        default="Pending"
    )

    payment_status = db.Column(
        db.String(30),
        default="Pending"
    )

    # ==========================
    # Razorpay Fields
    # ==========================

    razorpay_order_id = db.Column(
        db.String(120),
        unique=True,
        nullable=True
    )

    razorpay_payment_id = db.Column(
        db.String(120),
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    items = db.relationship(
        "OrderItem",
        backref="order",
        lazy=True,
        cascade="all, delete-orphan"
    )