from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from goats.models import Goat, GoatsInLoad
from loads.models import Load
from goats.serializer import GoatSerializer, GoatsInLoadSerializer
from loads.serializer import LoadSerializer
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def addGoatToLoad(request, id):
    if request.method == 'POST':
        body = json.loads(request.body.decode("utf-8"))
        
        GoatSerializerObj = GoatSerializer(data = body)
        loadobj = Load.objects.get(id = id)
        loadobj.goat_count += 1
        
        if (body['sex'] == 'Male'):
            loadobj.num_male += 1
        else:
            loadobj.num_female += 1
        loadobj.value_load += float(body['price'])
        loadobj.save()
        if GoatSerializerObj.is_valid():
            goatserialized = GoatSerializerObj.save()
            
            obj = dict()
            obj = { 'load_id': id, 'goat_id': goatserialized.id, 'status': True}
            gtlobj = GoatsInLoadSerializer(data = obj)
            if gtlobj.is_valid():
                gtlobj.save()
            return JsonResponse( {'status':'200', 'msg': 'Goat details added to current load'})
        return JsonResponse( {'status':'400', 'msg': 'Goat details are missing'})
               
 
@csrf_exempt
def getGoats(request, id):      
    if request.method == 'GET':
        goat_ids = list(GoatsInLoad.objects.filter(load_id = id, status = True).values('goat_id'))
        clean_ids = []
        for g in goat_ids:
            clean_ids.append( g['goat_id'])
        data = list (Goat.objects.filter(pk__in = clean_ids).values_list())
        result = []
        for i in data:
            temp = dict()
            temp['id'] = i[0]
            temp['sex'] = i[1]
            temp['breed'] = i[2]
            temp['weight'] = i[3]
            temp['photo_url'] = i[4]
            result.append(temp)
        return JsonResponse({'status':'200', 'msg': 'All Goat details have been fetched', 'data':result})
    return JsonResponse({'status':'400', 'msg': 'Goat details are missing'})
  
        
        
@csrf_exempt
def createLoad(request):
    if request.method == 'POST':
        body = dict()
        body['goat_count'] = 0
        body['num_male'] = 0
        body['num_female'] = 0
        LoadSerialObj = LoadSerializer(data = body)
        print(LoadSerialObj.is_valid())
        if LoadSerialObj.is_valid():
            LoadSerialObj.save()
            return JsonResponse( {'status':'200', 'msg': 'New Load created'})
        return JsonResponse( {'status':'400', 'msg': 'Load could not be created'})
    
@csrf_exempt
def getAllLoads(request):
    if request.method == 'GET':
        data = list (Load.objects.filter(status='True').values())
        return JsonResponse({'status':'200', 'msg': 'All Load details have been fetched', 'data':data})
    return JsonResponse({'status':'400', 'msg': 'Load details could not be fetched'})
    
    
@csrf_exempt
def mergeLoads(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode("utf-8"))
        print(body['data'])
        
        # create load
        load = dict()
        load['goat_count'] = 0
        load['num_male'] = 0
        load['num_female'] = 0
        
        LoadSerialObj = LoadSerializer(data = load)

        if LoadSerialObj.is_valid():
            LoadSerialized = LoadSerialObj.save()
            print(LoadSerialized.id)
            for load in body['data']:
                loadobj = Load.objects.get(id = load)
                loadobj.status = False
                loadobj.save()
                prevMapping = GoatsInLoad.objects.filter(load_id = load)
                for i in prevMapping:
                    
                    i.status = False
                    i.save()
                    # create new mapping
                    obj = dict()
                    obj = { 'load_id': LoadSerialized.id, 'goat_id': i.goat_id, 'status': True}
                    goatobj = Goat.objects.get(id = i.goat_id)
                    newloadobj = Load.objects.get(id = LoadSerialized.id)
                    newloadobj.goat_count += 1
                    newloadobj.value_load += goatobj.price
                    if goatobj.sex  == 'Male':
                        newloadobj.num_male += 1
                    else:
                        newloadobj.num_female += 1
                    newloadobj.save()
                    gtlobj = GoatsInLoadSerializer(data = obj)
                    if gtlobj.is_valid():
                        gtlobj.save()
        return JsonResponse({'status':'200', 'msg': 'Merge successful'})
    return JsonResponse({'status':'400', 'msg': 'Merge failed'})
    
    
@csrf_exempt
def splitLoad(request, id):
    if request.method == 'POST':
        body = json.loads(request.body.decode("utf-8"))
        print(body['data'])
        for group in body['data']:
            # create load
            load = dict()
            load['goat_count'] = 0
            load['num_male'] = 0
            load['num_female'] = 0
            
            LoadSerialObj = LoadSerializer(data = load)

            if LoadSerialObj.is_valid():
                LoadSerialized = LoadSerialObj.save()
                for goat in group:
                    
                    # change prev mapping to false
                    globj = GoatsInLoad.objects.get(goat_id = goat,status = True)
                    globj.status = False
                    globj.save()
                    
                    
                    prevLoadobj = Load.objects.get(id = globj.load_id)
                    prevLoadobj.status = False
                    prevLoadobj.save()
                    
                    # create new mapping
                    obj = dict()
                    obj = { 'load_id': LoadSerialized.id, 'goat_id': goat, 'status': True}
                    goatobj = Goat.objects.get(id = goat)
                    
                    #update new load object
                    newloadobj = Load.objects.get(id = LoadSerialized.id)
                    newloadobj.goat_count += 1
                    newloadobj.value_load += goatobj.price
                    if goatobj.sex  == 'Male':
                        newloadobj.num_male += 1
                    else:
                        newloadobj.num_female += 1
                    newloadobj.save()
                    
                    #save new mapping
                    gtlobj = GoatsInLoadSerializer(data = obj)
                    if gtlobj.is_valid():
                        gtlobj.save()
                
        return JsonResponse({'status':'200', 'msg': 'Split successful'})
    return JsonResponse({'status':'400', 'msg': 'Split process failed'})
