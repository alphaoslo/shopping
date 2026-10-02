"""
Category Services

Business logic for Category Management.
"""

from models import db, Category, Product


class CategoryService:

    @staticmethod
    def get_all():
        return Category.query.order_by(Category.name.asc()).all()

    @staticmethod
    def get_by_id(category_id):
        return Category.query.get_or_404(category_id)

    @staticmethod
    def name_exists(name, exclude_id=None):
        query = Category.query.filter(Category.name == name)
        if exclude_id:
            query = query.filter(Category.id != exclude_id)
        return query.first() is not None

    @staticmethod
    def create(name, description, image):
        category = Category(
            name=name,
            description=description,
            image=image,
        )
        db.session.add(category)
        db.session.commit()
        return category

    @staticmethod
    def update(category, name, description, image=None):
        category.name = name
        category.description = description
        if image:
            category.image = image
        db.session.commit()
        return category

    @staticmethod
    def delete(category):
        if category.products:
            return False, "Cannot delete category with products."
        db.session.delete(category)
        db.session.commit()
        return True, "Category deleted."
