import os


class Config:
    """
    Base configuration shared across all environments.
    """

    # =====================================================
    # Base Project Directory
    # =====================================================

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # =====================================================
    # Database Configuration
    # =====================================================

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(
            BASE_DIR,
            "instance",
            "paint_store.db",
        ),
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # =====================================================
    # Security
    # =====================================================

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "your-secret-key-change-this-later",
    )

    # =====================================================
    # Razorpay
    # =====================================================

    RAZORPAY_KEY_ID = os.environ.get(
        "RAZORPAY_KEY_ID",
        "rzp_test_TK8xBHeMD5dt1X",
    )

    RAZORPAY_KEY_SECRET = os.environ.get(
        "RAZORPAY_KEY_SECRET",
        "H0Ec7nd6zVukTcDRRQ8jGZlL",
    )

    # =====================================================
    # Upload Configuration
    # =====================================================

    UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        "static",
        "uploads",
    )

    PRODUCT_UPLOAD_FOLDER = os.path.join(
        UPLOAD_FOLDER,
        "products",
    )

    BRAND_UPLOAD_FOLDER = os.path.join(
        UPLOAD_FOLDER,
        "brands",
    )

    CATEGORY_UPLOAD_FOLDER = os.path.join(
        UPLOAD_FOLDER,
        "categories",
    )

    ALLOWED_IMAGE_EXTENSIONS = {
        "png",
        "jpg",
        "jpeg",
        "webp",
    }


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True