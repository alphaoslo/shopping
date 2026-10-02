from functools import wraps

from flask import (
    session,
    redirect,
    url_for,
    flash,
)


def admin_required(view_function):
    """
    Protect admin routes.
    Redirect unauthenticated users to the admin login page.
    """

    @wraps(view_function)
    def wrapper(*args, **kwargs):

        if "admin_id" not in session:

            flash(
                "Please log in to continue.",
                "warning",
            )

            return redirect(
                url_for("admin.admin_auth.login")
            )

        return view_function(*args, **kwargs)

    return wrapper