from flask import Blueprint

brands_bp = Blueprint(
    "brands",
    __name__,
    url_prefix="/brands",
)
