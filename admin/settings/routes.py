from flask import render_template, request, flash, redirect, url_for, session

from admin.settings import settings_bp
from utils.auth import admin_required


@settings_bp.route("/", methods=["GET", "POST"])
@admin_required
def index():
    if request.method == "POST":
        store_name = request.form.get("store_name", "").strip()
        contact_email = request.form.get("contact_email", "").strip()
        contact_phone = request.form.get("contact_phone", "").strip()
        low_stock_threshold = request.form.get("low_stock_threshold", "5").strip()

        if not store_name:
            flash("Store name is required.", "danger")
            return render_template("admin/settings/index.html")

        session["store_settings"] = {
            "store_name": store_name,
            "contact_email": contact_email,
            "contact_phone": contact_phone,
            "low_stock_threshold": low_stock_threshold,
        }

        flash("Settings saved successfully!", "success")
        return redirect(url_for("admin.settings.index"))

    settings = session.get("store_settings", {
        "store_name": "Color Joys Paint Co.",
        "contact_email": "",
        "contact_phone": "",
        "low_stock_threshold": "5",
    })

    return render_template(
        "admin/settings/index.html",
        settings=settings,
    )
