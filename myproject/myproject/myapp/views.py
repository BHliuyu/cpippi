from django.shortcuts import render
from django.http.response import JsonResponse
from . import models
from django.core.serializers import serialize
import json

# Create your views here.

def home(request):
    return render(request, "index.html")

def get_cpi_yoy(request):
    data = {}
    ret = models.Cpi.objects.all().values()
    data["data"] = list(ret)
    return JsonResponse(data, safe=False)

def get_ppi_yoy(request):
    data = {}
    ret = models.Ppi.objects.all().values()
    data["data"] = list(ret)
    return JsonResponse(data, safe=False)

def get_cpi_mom(request):
    data = {}
    ret = models.CpiMom.objects.all().values()
    data["data"] = list(ret)
    return JsonResponse(data, safe=False)

def get_ppi_mom(request):
    data = {}
    ret = models.PpiMom.objects.all().values()
    data["data"] = list(ret)
    return JsonResponse(data, safe=False)

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


def get_cpi_compare(request):
    data = {}
    ret = models.Cpicompare.objects.all().values()
    data["data"] = list(ret)
    return JsonResponse(data, safe=False)

def get_ppi_compare(request):
    data = {}
    ret = models.Ppicompare.objects.all().values()
    data["data"] = list(ret)
    return JsonResponse(data, safe=False)
