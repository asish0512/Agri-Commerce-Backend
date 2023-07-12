from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
from logistics.models import Logistics
from goats.models import GoatsInLoad, Goat
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def getGoatsDest(request, place):
    if request.method == 'GET':
    
        # get all load proceeding to a dest
        goatids = []
        logisticsobj = Logistics.objects.filter(destination = place)
        for i in logisticsobj:
            goatobj = GoatsInLoad.objects.filter(load_id = i.load_id, status = True)
            for g in goatobj:
                goatids.append(g.goat_id)
        data = list(Goat.objects.filter(id__in = goatids).values())
        return JsonResponse({'status':'200', 'msg': 'All goats at a destination have been fetched', 'data':data})
    return JsonResponse({'status':'400', 'msg': 'goat details could not be fetched'})



@csrf_exempt
def buyGoats(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode("utf-8"))
        
        for goatid in body['data']:
            globj = GoatsInLoad.objects.get(goat_id=goatid, status = True)
            globj.status = False
            globj.save()
        
        return JsonResponse( {'status':'200', 'msg': 'Goats have been purchased'})
    return JsonResponse( {'status':'400', 'msg': 'Goats purchase didnt succeed'})
