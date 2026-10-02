from models import db


class Brand(db.Model):
    __tablename__ = "brands"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False, unique=True)

    description = db.Column(db.Text)

    logo = db.Column(db.String(255))

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    # One Brand -> Many Products
    products = db.relationship(
        "Product",
        back_populates="brand",
        lazy=True
    )

    def __repr__(self):
        return f"<Brand {self.name}>"