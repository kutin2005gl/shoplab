"""URL của bản Secure (chọn bằng ROOT_URLCONF trong settings/secure.py)."""
from django.urls import include, path

# Django Admin (/admin/) cố ý không được route ở đây: chưa dùng tới, bớt một cửa để tấn công.
urlpatterns = [
    # Mọi API đều nằm dưới tiền tố /api/v1/.
    path('api/v1/', include('apps.core.urls')),
]
