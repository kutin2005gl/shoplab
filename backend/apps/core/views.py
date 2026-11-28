"""Endpoint hệ thống: kiểm tra server còn sống (health) và đang chạy bản nào (meta)."""
import logging

from django.conf import settings
from django.db import DatabaseError, InterfaceError, connection
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class HealthView(APIView):
    """GET /api/v1/health — API và database có đang hoạt động không?"""

    # Endpoint công khai nên phải ghi rõ AllowAny (mặc định của dự án là cấm).
    permission_classes = [AllowAny]
    # Không đọc session/user: nếu đọc, lúc DB hỏng request sẽ lỗi trước khi vào get().
    authentication_classes = []

    def get(self, request):
        try:
            # Câu SQL rẻ nhất có thể, chỉ để biết DB có trả lời không.
            with connection.cursor() as cursor:
                cursor.execute('SELECT 1')
                cursor.fetchone()
        except (DatabaseError, InterfaceError):
            # Chi tiết lỗi (host, user DB...) chỉ ghi vào log, KHÔNG trả cho client.
            logger.exception('Health check: không kết nối được database')
            # 503 Service Unavailable: công cụ giám sát dựa vào mã này để biết có sự cố.
            return Response({'status': 'error', 'db': 'error'}, status=503)
        return Response({'status': 'ok', 'db': 'ok'})


class MetaView(APIView):
    """GET /api/v1/meta — frontend dùng để hiện banner tên bản đang chạy."""

    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        # Chỗ DUY NHẤT được đọc tên variant (ARCHITECTURE mục 3.2, luật 5).
        return Response({'variant': settings.SHOPLAB_VARIANT})
