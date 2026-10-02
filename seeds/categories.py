from models import db
from models.category import Category


def seed_categories():

    if Category.query.first():
        print("Categories already exist.")
        return

    categories = [

        Category(
            name="Interior Paints",
            description="Premium paints for interior walls.",
            image="interior.png"
        ),

        Category(
            name="Exterior Paints",
            description="Weather-resistant exterior paints.",
            image="exterior.png"
        ),

        Category(
            name="Primers",
            description="Primers for smooth and durable paint finishes.",
            image="primer.png"
        ),

        Category(
            name="Wood Coatings",
            description="Premium finishes for wooden surfaces.",
            image="wood.png"
        ),

        Category(
            name="Waterproofing",
            description="Protect walls and roofs from water damage.",
            image="waterproof.png"
        ),

        Category(
            name="Painting Tools",
            description="Brushes, rollers, trays and accessories.",
            image="tools.png"
        )

    ]

    db.session.add_all(categories)
    db.session.commit()

    print("Categories inserted successfully.")