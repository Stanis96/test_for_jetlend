import time

from rest_framework.decorators import api_view
from django.db import transaction
from rest_framework.response import Response

from .models import Investor
from .tasks import investor_task


@transaction.atomic
@api_view(['POST'])
def api_create_investor(request):
  investor = Investor.objects.create()
  transaction.on_commit(lambda: investor_task.delay(investor.id))

  time.sleep(0.5)
  return Response({"status": "OK"})
