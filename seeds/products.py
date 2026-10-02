from models import db
from models.product import Product
from models.category import Category
from models.brand import Brand


def seed_products():

    # Remove existing products
    Product.query.delete()
    db.session.commit()
    

    interior = Category.query.filter_by(name="Interior Paints").first()
    exterior = Category.query.filter_by(name="Exterior Paints").first()
    primer = Category.query.filter_by(name="Primers").first()
    wood = Category.query.filter_by(name="Wood Coatings").first()
    waterproof = Category.query.filter_by(name="Waterproofing").first()

    asian = Brand.query.filter_by(name="Asian Paints").first()
    berger = Brand.query.filter_by(name="Berger Paints").first()
    nerolac = Brand.query.filter_by(name="Nerolac").first()
    dulux = Brand.query.filter_by(name="Dulux").first()
    indigo = Brand.query.filter_by(name="Indigo Paints").first()
    nippon = Brand.query.filter_by(name="Nippon Paint").first()

    products = [

        Product(
            name="Premium Acrylic Emulsion",
            description="Premium washable interior emulsion.",
            price=1999,
            original_price=2499,
            rating=4.8,
            review_count=128,
            stock=50,
            image="jeevan-premium-emulsion.png",
            is_featured=True,
            is_best_seller=True,
            category=interior,
            brand=asian
        ),

        Product(
            name="Exterior Weather Shield",
            description="Long-lasting exterior protection.",
            price=2299,
            original_price=2499,
            rating=4.8,
            review_count=128,
            stock=40,
            image="jeevan-premium-emulsion.png",
            is_featured=True,
            is_best_seller=True,
            category=exterior,
            brand=berger
        ),

        Product(
            name="Wall Primer",
            description="Smooth base coat before painting.",
            price=999,
            original_price=2799,
            rating=4.7,
            review_count=96,
            stock=60,
            image="jeevan-premium-emulsion.png",
            is_featured=True,
            is_best_seller=False,
            category=primer,
            brand=nerolac
        ),

        Product(
            name="Luxury Interior Paint",
            description="Rich matte finish for modern homes.",
            price=2499,
            original_price=2799,
            rating=4.7,
            review_count=96,
            stock=35,
            image="jeevan-premium-emulsion.png",
            is_featured=True,
            is_best_seller=True,
            category=interior,
            brand=dulux
        ),

        Product(
            name="Wood Finish",
            description="Premium finish for wooden furniture.",
            price=1499,
            original_price=1799,
            rating=4.7,
            review_count=52,
            stock=25,
            image="jeevan-premium-emulsion.png",
            is_featured=False,
            is_best_seller=True,
            category=wood,
            brand=indigo
        ),

        Product(
            name="Waterproof Coating",
            description="Protect walls from moisture damage.",
            price=1799,
            original_price=2199,
            rating=4.8,
            review_count=61,
            stock=30,
            image="jeevan-premium-emulsion.png",
            is_featured=False,
            is_best_seller=True,
            category=waterproof,
            brand=nippon
        ),

        Product(
            name="Ceiling White",
            description="Bright white ceiling paint with smooth finish.",
            price=1299,
            original_price=1599,
            rating=4.5,
            review_count=39,
            stock=45,
            image="jeevan-premium-emulsion.png",
            is_featured=True,
            is_best_seller=False,
            category=interior,
            brand=asian
        ),

        Product(
            name="Texture Finish",
            description="Decorative textured wall finish.",
            price=2699,
            original_price=3199,
            rating=4.9,
            review_count=147,
            stock=20,
            image="jeevan-premium-emulsion.png",
            is_featured=True,
            is_best_seller=False,
            category=interior,
            brand=dulux
        ),

        Product(
            name="Premium Exterior Primer",
            description="High adhesion primer for exterior walls.",
            price=1199,
            original_price=1499,
            rating=4.6,
            review_count=73,
            stock=55,
            image="jeevan-premium-emulsion.png",
            is_featured=True,
            is_best_seller=False,
            category=primer,
            brand=berger
        ),

        Product(
            name="Luxury Wood Polish",
            description="Premium wood coating with glossy finish.",
            price=1899,
            original_price=2299,
            rating=4.8,
            review_count=58,
            stock=30,
            image="jeevan-premium-emulsion.png",
            is_featured=True,
            is_best_seller=False,
            category=wood,
            brand=indigo
        ),

    ]

    db.session.add_all(products)
    db.session.commit()

    print("Products inserted successfully.")