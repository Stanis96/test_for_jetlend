from celery import shared_task
from django.db import transaction

from .models import Investor


@shared_task
def investor_task(investor_id):
  with transaction.atomic():
    investor = Investor.objects.get(pk=investor_id)
    investor.processed = True
    investor.save()
    raise Exception({"status": "OK"})
