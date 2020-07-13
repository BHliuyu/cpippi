from django.shortcuts import render
from django.http.response import JsonResponse
from . import models
from django.core.serializers import serialize
import json

# Create your views here.

def home(request):
    return render(request, "index.html")

def get_cpidata_api(request):

    data = {}
    ret = models.CpiHighFreqData.objects.all().values()
    data["data"] = list(ret)
    return JsonResponse(data, safe=False)

def get_ppidata_api(request):

    data = {}
    ret = models.PpiHighFreqData.objects.all().values()
    data["data"] = list(ret)
    return JsonResponse(data, safe=False)

def get_cpippi_api(request):

    data = {}
    ret = models.CpiPpi.objects.all().values()
    data["data"] = list(ret)
    return JsonResponse(data, safe=False)
