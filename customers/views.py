from .models import *
from .serializers import *
from django.http import JsonResponse, Http404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def customers(request):
  if request.method == 'GET':
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    context = {'customers': serializer.data}
    return Response(context)
  elif request.method == 'POST':
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      context = {'customers': serializer.data}
      return Response(context, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def customer(request,id):
  try:
    data = Customer.objects.get(pk=id)
  except Customer.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
    
  if request.method == 'GET':
    serializer = CustomerSerializer(data)
    context = {'customer': serializer.data}
    return Response(context)
  elif request.method == 'DELETE':
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  elif request.method == "POST":
    serializer = CustomerSerializer(data, data=request.data)
    if serializer.is_valid():
      serializer.save()
      context = {'customer': serializer.data}
      return Response(context)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)