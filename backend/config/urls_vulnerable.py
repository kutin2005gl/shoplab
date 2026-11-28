"""URL của bản Vulnerable (chọn bằng ROOT_URLCONF trong settings/vulnerable.py)."""
from django.urls import include, path

urlpatterns = [
    # Từ Phase 11, route bị làm yếu đặt Ở ĐÂY, phía trên: Django lấy route khớp ĐẦU TIÊN.
    # Phần còn lại dùng chung với bản Secure.
    path('', include('config.urls_secure')),
]
