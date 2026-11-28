from django.urls import path

from . import views

urlpatterns = [
    # Ghép với tiền tố ở config/urls_secure.py thành /api/v1/health và /api/v1/meta.
    path('health', views.HealthView.as_view()),
    path('meta', views.MetaView.as_view()),
]
