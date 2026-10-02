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

from models import db, Brand
from admin.brands import brands_bp
from admin.brands.services import BrandService
from utils.auth import admin_required


@brands_bp.route("/")
@admin_required
def index():
    brands = BrandService.get_all()
    return render_template(
        "admin/brands/list.html",
        brands=brands,
    )


@brands_bp.route("/create", methods=["GET", "POST"])
@admin_required
def create():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()

        if not name:
            flash("Brand name is required.", "danger")
            return render_template("admin/brands/create.html")

        if BrandService.name_exists(name):
            flash("A brand with this name already exists.", "danger")
            return render_template("admin/brands/create.html")

        logo_filename = _save_image(request.files.get("logo"))

        BrandService.create(name, description, logo_filename)
        flash("Brand added successfully!", "success")
        return redirect(url_for("admin.brands.index"))

    return render_template("admin/brands/create.html")


@brands_bp.route("/<int:brand_id>/edit", methods=["GET", "POST"])
@admin_required
def edit(brand_id):
    brand = BrandService.get_by_id(brand_id)

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()

        if not name:
            flash("Brand name is required.", "danger")
            return render_template("admin/brands/edit.html", brand=brand)

        if BrandService.name_exists(name, exclude_id=brand.id):
            flash("A brand with this name already exists.", "danger")
            return render_template("admin/brands/edit.html", brand=brand)

        logo_filename = _save_image(request.files.get("logo"))

        BrandService.update(brand, name, description, logo_filename)
        flash("Brand updated successfully!", "success")
        return redirect(url_for("admin.brands.index"))

    return render_template("admin/brands/edit.html", brand=brand)


@brands_bp.route("/<int:brand_id>/delete", methods=["POST"])
@admin_required
def delete(brand_id):
    brand = BrandService.get_by_id(brand_id)
    ok, message = BrandService.delete(brand)
    flash(message, "success" if ok else "danger")
    return redirect(url_for("admin.brands.index"))


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
    folder = current_app.config["BRAND_UPLOAD_FOLDER"]
    os.makedirs(folder, exist_ok=True)
    image_file.save(os.path.join(folder, filename))
    return filename
