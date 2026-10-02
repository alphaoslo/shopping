from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
)

from admin.auth.services import AdminAuthService


admin_auth_bp = Blueprint(
    "admin_auth",
    __name__,
)


@admin_auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """
    Admin Login
    """
    if "admin_id" in session:
        return redirect(
            url_for("admin.admin_routes.dashboard")
        )

    if request.method == "POST":

        login = request.form.get("login", "").strip()

        password = request.form.get("password", "")

        admin = AdminAuthService.authenticate(login, password)

        if admin:

            session["admin_id"] = admin.id

            flash(
                "Welcome back!",
                "success",
            )

            return redirect(
                url_for("admin.admin_routes.dashboard")
            )

        flash(
            "Invalid username/email or password.",
            "danger",
        )

    return render_template(
        "admin/auth/login.html"
    )

@admin_auth_bp.route("/logout")
def logout():
    """
    Admin Logout
    """

    session.pop("admin_id", None)

    flash(
        "You have been logged out successfully.",
        "success",
    )

    return redirect(
        url_for("admin.admin_auth.login")
    )