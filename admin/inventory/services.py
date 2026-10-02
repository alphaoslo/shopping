"""
Inventory Services

Business logic for Inventory Management.
"""

from models import db, Product

LOW_STOCK_THRESHOLD = 5


class InventoryService:

    @staticmethod
    def get_all_products():
        return Product.query.order_by(Product.name.asc()).all()

    @staticmethod
    def get_low_stock():
        return (
            Product.query
            .filter(Product.stock <= LOW_STOCK_THRESHOLD)
            .order_by(Product.stock.asc())
            .all()
        )

    @staticmethod
    def get_out_of_stock():
        return (
            Product.query
            .filter(Product.stock <= 0)
            .order_by(Product.name.asc())
            .all()
        )

    @staticmethod
    def update_stock(product_id, quantity):
        product = Product.query.get_or_404(product_id)
        try:
            quantity = int(quantity)
        except (ValueError, TypeError):
            return None, "Invalid quantity."

        if quantity < 0:
            return None, "Stock cannot be negative."

        product.stock = quantity
        db.session.commit()
        return product, "Stock updated."
