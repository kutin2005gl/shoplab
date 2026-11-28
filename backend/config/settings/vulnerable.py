"""Settings của bản Vulnerable (chỉ chạy local). Chọn bằng DJANGO_SETTINGS_MODULE=config.settings.vulnerable.

Hiện chưa có lỗi nào. Mỗi cấu hình yếu thêm sau này phải có comment `# VULN-xxx`
và file labs/VULN-xxx-*.md tương ứng.
"""
from .base import *  # noqa: F401,F403

ROOT_URLCONF = 'config.urls_vulnerable'

# Chỉ dùng để GET /api/v1/meta trả về. KHÔNG dùng để rẽ nhánh logic.
SHOPLAB_VARIANT = 'vulnerable'
