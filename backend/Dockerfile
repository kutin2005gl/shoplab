# Dockerfile — công thức build image cho backend Django (PR-004).
# Chạy từng dòng từ trên xuống; mỗi dòng RUN/COPY tạo một "layer" được cache lại.

# Image gốc: Python 3.12 (D-017), bản "slim" = Debian rút gọn, nhỏ hơn bản đầy đủ.
FROM python:3.12-slim

# Không ghi file .pyc vào đĩa (container không cần) và in log ra ngay, không đệm lại.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Thư mục làm việc trong container; các lệnh bên dưới chạy ở đây.
WORKDIR /app

# Chỉ copy requirements.txt TRƯỚC, rồi mới cài thư viện.
# Nhờ vậy khi chỉ sửa code, Docker dùng lại layer đã cài, build nhanh hơn nhiều.
COPY requirements.txt .

# --no-cache-dir: không giữ cache của pip trong image, image nhẹ hơn.
RUN pip install --no-cache-dir -r requirements.txt

# Copy code Django (manage.py, config/...) vào image. Đặt SAU khi cài thư viện
# để sửa code không làm mất cache của bước pip install ở trên.
COPY . .

# Lệnh mặc định tạm: in phiên bản Python. PR-009 sẽ đổi thành lệnh chạy server.
CMD ["python", "--version"]
