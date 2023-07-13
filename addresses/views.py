from django.shortcuts import render
from .models import Addresses
from .serializers import AddressesSerializers
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def address_list(req):
    if req.method == 'GET':
        query_set = Addresses.objects.all()
        serializer = AddressesSerializers(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif req.method == 'POST':
        data = JSONParser().parse(req)
        serializer = AddressesSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def address(req, id):
    obj = Addresses.objects.get(id=id)

    if req.method == 'GET':
        serializer = AddressesSerializers(obj)
        return JsonResponse(serializer.data, safe=False)
        
    elif req.method == 'PUT':
        data = JSONParser().parse(req)
        serializer = AddressesSerializers(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.error, status=400)
    
    elif req.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=200)