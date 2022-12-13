from .models import *
from .serializers import *
from django.http import JsonResponse

def customers(request):
  data = Customer.objects.all()
  serializer = CustomerSerializer(data, many=True)
  context = {'customers': serializer.data}
  return JsonResponse(context)