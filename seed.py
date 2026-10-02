from flask import Flask

from config import Config
from models import db

from seeds.categories import seed_categories
from seeds.brands import seed_brands
from seeds.products import seed_products
from seeds.admin import seed_admin


app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)


def main():
    with app.app_context():

        print("=" * 50)
        print("Creating Database Tables...")
        print("=" * 50)

        db.create_all()

        print("=" * 50)
        print("Seeding Database...")
        print("=" * 50)

        seed_categories()
        seed_brands()
        seed_products()
        seed_admin()

        print("=" * 50)
        print("Database Seeding Completed.")
        print("=" * 50)


if __name__ == "__main__":
    main()