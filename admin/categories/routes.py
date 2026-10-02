import os
import uuid

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    current_app,
)
from werkzeug.utils import secure_filename

from models import db, Category
from admin.categories import categories_bp
from admin.categories.services import CategoryService
from utils.auth import admin_required


@categories_bp.route("/")
@admin_required
def index():
    categories = CategoryService.get_all()
    return render_template(
        "admin/categories/list.html",
        categories=categories,
    )


@categories_bp.route("/create", methods=["GET", "POST"])
@admin_required
def create():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()

        if not name:
            flash("Category name is required.", "danger")
            return render_template("admin/categories/create.html")

        if CategoryService.name_exists(name):
            flash("A category with this name already exists.", "danger")
            return render_template("admin/categories/create.html")

        image_filename = _save_image(request.files.get("image"))

        CategoryService.create(name, description, image_filename)
        flash("Category added successfully!", "success")
        return redirect(url_for("admin.categories.index"))

    return render_template("admin/categories/create.html")


@categories_bp.route("/<int:category_id>/edit", methods=["GET", "POST"])
@admin_required
def edit(category_id):
    category = CategoryService.get_by_id(category_id)

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()

        if not name:
            flash("Category name is required.", "danger")
            return render_template("admin/categories/edit.html", category=category)

        if CategoryService.name_exists(name, exclude_id=category.id):
            flash("A category with this name already exists.", "danger")
            return render_template("admin/categories/edit.html", category=category)

        image_filename = _save_image(request.files.get("image"))

        CategoryService.update(category, name, description, image_filename)
        flash("Category updated successfully!", "success")
        return redirect(url_for("admin.categories.index"))

    return render_template("admin/categories/edit.html", category=category)


@categories_bp.route("/<int:category_id>/delete", methods=["POST"])
@admin_required
def delete(category_id):
    category = CategoryService.get_by_id(category_id)
    ok, message = CategoryService.delete(category)
    flash(message, "success" if ok else "danger")
    return redirect(url_for("admin.categories.index"))


def _save_image(image_file):
    if not image_file or not image_file.filename:
        return None

    original_filename = secure_filename(image_file.filename)
    extension = os.path.splitext(original_filename)[1].lower()
    allowed = current_app.config["ALLOWED_IMAGE_EXTENSIONS"]

    if extension.lstrip(".") not in allowed:
        flash("Invalid image format.", "danger")
        return None

    filename = f"{uuid.uuid4().hex}{extension}"
    folder = current_app.config["CATEGORY_UPLOAD_FOLDER"]
    os.makedirs(folder, exist_ok=True)
    image_file.save(os.path.join(folder, filename))
    return filename
