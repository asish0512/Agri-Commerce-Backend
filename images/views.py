from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from images.models import Image
from images.serializer import ImageSerializer
from django.views.decorators.csrf import csrf_exempt
import json
import jsonpickle

# Create your views here.
@csrf_exempt
def getAnnots(request, goatId):
    if request.method == 'GET':
        data = list (Image.objects.filter(goat_id = goatId).values())
        result = []
        
        for i in data:
            result.append( json.loads( jsonpickle.decode(  json.dumps(i['image']))))
            
        return JsonResponse({'status':'200', 'msg': 'All Load details have been fetched', 'data':result})
    return JsonResponse({'status':'400', 'msg': 'Load details could not be fetched'})



@csrf_exempt
def addAnnot(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode("utf-8"))
        
        dataobj = dict()
        dataobj['goat_id'] = body['goat_id']
        dataobj['image'] =  json.dumps( body['data'])
        
        ImageSerialObj = ImageSerializer(data = dataobj)
        if ImageSerialObj.is_valid():
            ImageSerialObj.save()     
            
        return JsonResponse( {'status':'200', 'msg': 'Goat details added to current load'})
    return JsonResponse( {'status':'400', 'msg': 'Goat details are missing'})
