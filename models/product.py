from models import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150), nullable=False)
    sku = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    description = db.Column(db.Text)

    price = db.Column(db.Float, nullable=False)

    original_price = db.Column(db.Float, nullable=False)
    discount = db.Column(
        db.Float,
        default=0
    )
    rating = db.Column(
    db.Float,
    default=5.0
    )
    review_count = db.Column(
    db.Integer,
    default=0
    )

    stock = db.Column(db.Integer, default=0)

    image = db.Column(db.String(255))

    is_active = db.Column(
       db.Boolean,
       default=True
    )

    is_featured = db.Column(db.Boolean, default=False)

    is_best_seller = db.Column(db.Boolean, default=False)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    # Foreign Keys
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False
    )

    brand_id = db.Column(
        db.Integer,
        db.ForeignKey("brands.id"),
        nullable=False
    )

    # Relationships
    category = db.relationship(
        "Category",
        back_populates="products"
    )

    brand = db.relationship(
        "Brand",
        back_populates="products"
    )

    def __repr__(self):
        return f"<Product {self.name}>"