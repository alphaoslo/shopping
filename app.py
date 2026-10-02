import os
from flask import Flask
from flask_migrate import Migrate

from config import DevelopmentConfig, ProductionConfig
from models import db
from admin import admin_bp
from customer.routes import customer_bp

# ---------------------------------------------------------
# Application Initialization
# ---------------------------------------------------------

app = Flask(__name__)

# Load Application Configuration (production when deployed)
if os.environ.get("FLASK_ENV") == "production" or os.environ.get("RENDER"):
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

# Initialize Extensions
db.init_app(app)
migrate = Migrate(app, db)

# ---------------------------------------------------------
# Register Blueprints
# ---------------------------------------------------------

app.register_blueprint(customer_bp)
app.register_blueprint(admin_bp)


# ---------------------------------------------------------
# Initialize database tables + default admin on startup
# ---------------------------------------------------------

with app.app_context():
    db.create_all()
    try:
        from seeds.admin import seed_admin
        seed_admin()
    except Exception:
        pass



# ---------------------------------------------------------
# Application Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)