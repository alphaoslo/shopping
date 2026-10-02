"""
Brand Services

Business logic for Brand Management.
"""

from models import db, Brand


class BrandService:

    @staticmethod
    def get_all():
        return Brand.query.order_by(Brand.name.asc()).all()

    @staticmethod
    def get_by_id(brand_id):
        return Brand.query.get_or_404(brand_id)

    @staticmethod
    def name_exists(name, exclude_id=None):
        query = Brand.query.filter(Brand.name == name)
        if exclude_id:
            query = query.filter(Brand.id != exclude_id)
        return query.first() is not None

    @staticmethod
    def create(name, description, logo):
        brand = Brand(
            name=name,
            description=description,
            logo=logo,
        )
        db.session.add(brand)
        db.session.commit()
        return brand

    @staticmethod
    def update(brand, name, description, logo=None):
        brand.name = name
        brand.description = description
        if logo:
            brand.logo = logo
        db.session.commit()
        return brand

    @staticmethod
    def delete(brand):
        if brand.products:
            return False, "Cannot delete brand with products."
        db.session.delete(brand)
        db.session.commit()
        return True, "Brand deleted."
