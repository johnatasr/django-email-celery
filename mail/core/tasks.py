from celery.utils.log import get_task_logger
from django.conf import settings
from django.core.mail import send_mail

from mail.celery import app

logger = get_task_logger(__name__)


@app.task(name="email_confirmacao")
def email_confirmacao(token, id, email):
    logger.info('Criando a task..')
    subject = 'Obrigado por se cadastrar!'
    from_email = settings.EMAIL_HOST_USER
    message = f"http://localhost:8000/confirm/?confirmation_key={token}&id={id}"
    to = email

    send_mail(
        subject,
        message,
        from_email,
        [to],
        fail_silently=False,
    )

    logger.info('Terminando task..')
