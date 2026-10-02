from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from models import db


class Admin(db.Model):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(80),
        nullable=False,
        unique=True,
    )

    email = db.Column(
        db.String(120),
        nullable=False,
        unique=True,
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False,
    )

    is_active = db.Column(
        db.Boolean,
        nullable=False,
        default=True,
    )

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
    )

    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
    def set_password(self, password):
        """
        Hash and store the admin password.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Verify the provided password against the stored password hash.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<Admin {self.username}>"