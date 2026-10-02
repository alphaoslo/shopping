from flask import Blueprint

from admin.products.routes import products_bp
from admin.categories.routes import categories_bp
from admin.brands.routes import brands_bp
from admin.inventory.routes import inventory_bp
from admin.orders.routes import orders_bp
from admin.reports.routes import reports_bp
from admin.settings.routes import settings_bp

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin",
)

from admin.auth.routes import admin_auth_bp
from admin.routes import admin_routes_bp

admin_bp.register_blueprint(admin_auth_bp)
admin_bp.register_blueprint(admin_routes_bp)
admin_bp.register_blueprint(products_bp)
admin_bp.register_blueprint(categories_bp)
admin_bp.register_blueprint(brands_bp)
admin_bp.register_blueprint(inventory_bp)
admin_bp.register_blueprint(orders_bp)
admin_bp.register_blueprint(reports_bp)
admin_bp.register_blueprint(settings_bp)
