from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from logistics.models import Logistics
from logistics.serializer import LogisticsSerializer
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def addConsign(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode("utf-8"))
        
        LogisticsSerializerObj = LogisticsSerializer(data = body)

        if LogisticsSerializerObj.is_valid():
            LogisticsSerializerObj.save()
            
            return JsonResponse( {'status':'200', 'msg': 'Consignment details added'})
    return JsonResponse( {'status':'400', 'msg': 'Failed to add consignment details'})
    

@csrf_exempt
def getConsigns(request):      
    if request.method == 'GET':
        data = list (Logistics.objects.values())
        return JsonResponse({'status':'200', 'msg': 'All consignment details have been fetched', 'data':data})
    return JsonResponse({'status':'400', 'msg': 'Consignment details could not be fetched'})