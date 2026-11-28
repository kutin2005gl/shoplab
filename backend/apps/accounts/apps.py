from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # name = đường dẫn import (apps/accounts); label mặc định = "accounts" (phần cuối).
    # Label này là thứ AUTH_USER_MODEL = 'accounts.User' trỏ tới.
    name = 'apps.accounts'
