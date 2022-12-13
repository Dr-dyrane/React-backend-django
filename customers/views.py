from .models import *
from .serializers import *
from django.http import JsonResponse, Http404

def customers(request):
  data = Customer.objects.all()
  serializer = CustomerSerializer(data, many=True)
  context = {'customers': serializer.data}
  return JsonResponse(context)

def customer(request,id):
  try:
    data = Customer.objects.get(pk=id)
  except Customer.DoesNotExist:
    raise Http404('Customer does not exist')
  serializer = CustomerSerializer(data)
  context = {'customer': serializer.data}
  return JsonResponse(context)

