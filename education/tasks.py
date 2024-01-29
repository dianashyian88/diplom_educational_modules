from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from users.models import User


@shared_task
def send_mail_create_course(name):
    list_user = User.objects.all()
    for obj in list_user:
        send_mail(
            subject='Новый курс',
            message=f'Здравствуйте, {obj.username}'
                    f'У нас появился новый курс "{name}". Возможно, Вам будет интересно.'
                    f'Скорее переходите на сайт, чтобы ознакомиться!!!',
            from_email=EMAIL_HOST_USER,
            recipient_list=[obj.email],
            fail_silently=False,
        )
