from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from sell.models import Selltran
from sell.serializer import SellSerializer
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def getSells(request):
    if request.method == 'GET':
        data = list (Selltran.objects.values())
        return JsonResponse({'status':'200', 'msg': 'All Load details have been fetched', 'data':data})
    return JsonResponse({'status':'400', 'msg': 'Load details could not be fetched'})



@csrf_exempt
def addSeller(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode("utf-8"))
        
        SellSerializerObj = SellSerializer(data = body)

        if SellSerializerObj.is_valid():
            SellSerializerObj.save()
            return JsonResponse( {'status':'200', 'msg': 'Goat details added to current load'})
        return JsonResponse( {'status':'400', 'msg': 'Goat details are missing'})
