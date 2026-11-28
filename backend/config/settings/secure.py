"""Settings của bản Secure (bản chuẩn). Chọn bằng DJANGO_SETTINGS_MODULE=config.settings.secure."""
from .base import *  # noqa: F401,F403

# Không bao giờ bật DEBUG ở bản Secure: trang lỗi DEBUG làm lộ code, settings, câu SQL.
DEBUG = False

ROOT_URLCONF = 'config.urls_secure'

# Chỉ dùng để GET /api/v1/meta trả về. KHÔNG dùng để rẽ nhánh logic.
SHOPLAB_VARIANT = 'secure'

# PR-069 sẽ thêm hardening (cookie flags, security headers...) vào file này.
