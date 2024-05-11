from celery import shared_task
from apps.product.models import Send_Email

@shared_task
def send_contact_email(name, email, message):
    Send_Email.objects.create(name=name, email=email, message=message)