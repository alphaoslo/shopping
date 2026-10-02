from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy instance
db = SQLAlchemy()

# Import models
from models.category import Category
from models.brand import Brand
from models.product import Product
from models.order import Order
from models.order_item import OrderItem
from models.admin import Admin