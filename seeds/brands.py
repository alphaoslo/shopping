from models import db
from models.brand import Brand


def seed_brands():

    if Brand.query.first():
        print("Brands already exist.")
        return

    brands = [

        Brand(
            name="Asian Paints",
            description="India's leading paint manufacturer.",
            logo="asian-paints.png"
        ),

        Brand(
            name="Berger Paints",
            description="Premium decorative and industrial paints.",
            logo="berger.png"
        ),

        Brand(
            name="Nerolac",
            description="High-quality paints for homes and industries.",
            logo="nerolac.png"
        ),

        Brand(
            name="Dulux",
            description="International brand known for premium finishes.",
            logo="dulux.png"
        ),

        Brand(
            name="Indigo Paints",
            description="Innovative decorative paint solutions.",
            logo="indigo.png"
        ),

        Brand(
            name="Nippon Paint",
            description="Global leader in coating technologies.",
            logo="nippon.png"
        )

    ]

    db.session.add_all(brands)
    db.session.commit()

    print("Brands inserted successfully.")