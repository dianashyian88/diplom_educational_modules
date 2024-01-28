from users.models import User


def create_user(password, email, username, phone, city, telegram_id):
    """Функция создания пользователя"""
    user = User.objects.create(
        email=email,
        username=username,
        phone=phone,
        city=city,
        telegram_id=telegram_id,
        is_superuser=False,
        is_staff=False,
        is_active=True
    )

    user.set_password(password)
    user.save()
