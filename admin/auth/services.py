from sqlalchemy import or_

from models import Admin


class AdminAuthService:
    """
    Service class responsible for admin authentication.
    """

    @staticmethod
    def authenticate(login, password):
        """
        Authenticate an admin using either username or email.

        Returns:
            Admin object on successful authentication.
            None if authentication fails.
        """

        admin = Admin.query.filter(
            or_(
                Admin.username == login,
                Admin.email == login,
            )
        ).first()

        if admin is None:
            return None

        if not admin.is_active:
            return None

        if not admin.check_password(password):
            return None

        return admin