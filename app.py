from flask import Flask
from flask_migrate import Migrate

from config import DevelopmentConfig
from models import db
from admin import admin_bp
from customer.routes import customer_bp

# ---------------------------------------------------------
# Application Initialization
# ---------------------------------------------------------

app = Flask(__name__)

# Load Application Configuration
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
# Application Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)