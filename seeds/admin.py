from models import db, Admin


def seed_admin():
    """
    Seed the default administrator account.
    """

    existing_admin = Admin.query.filter_by(
        username="admin"
    ).first()

    if existing_admin:
        print("Default admin already exists.")
        return

    admin = Admin(
        username="admin",
        email="admin@colorjoys.com",
        is_active=True,
    )

    admin.set_password("Admin@123")

    db.session.add(admin)
    db.session.commit()

    print("Default admin created successfully.")