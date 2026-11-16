"""Settings của bản Secure (bản chuẩn). Chọn bằng DJANGO_SETTINGS_MODULE=config.settings.secure."""
from .base import *  # noqa: F401,F403

# Không bao giờ bật DEBUG ở bản Secure: trang lỗi DEBUG làm lộ code, settings, câu SQL.
DEBUG = False

# PR-069 sẽ thêm hardening (cookie flags, security headers...) vào file này.
