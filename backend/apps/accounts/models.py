from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User của ShopLab.

    Hiện chỉ kế thừa AbstractUser (username, password, email, is_staff...) và thêm
    một ràng buộc: email không được trùng. Phân quyền Customer/Staff/Admin dùng
    Django Groups + Permissions (D-012), nên chưa cần thêm cột "role" ở đây.
    Sau này cần thêm cột (số điện thoại, địa chỉ...) thì chỉ việc thêm vào class này.
    """

    # AbstractUser cho phép email trống và trùng. Ta muốn mỗi email chỉ một tài khoản
    # (cần cho đăng ký, quên mật khẩu). Thêm ràng buộc này về sau rất khó vì dữ liệu
    # cũ có thể đã trùng -> làm ngay từ migration đầu tiên.
    email = models.EmailField('email address', unique=True)
