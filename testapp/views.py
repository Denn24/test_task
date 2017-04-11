from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from testapp.CharCounter import calcCount
from testapp.Encoder import cEncode, cDecode



def cesar(request):

    return render(request, "index.html")

def ajax(request):
    encodeData = request.GET['input']
    key = request.GET['key']
    choise = request.GET['choise']
    response = None
    if choise == "encode":
        response = cEncode(encodeData, int(key))
    elif choise == "decode":
        response = cDecode(encodeData, int(key))
    map = calcCount(encodeData)
    data = {'response': response, 'map':map}

    return JsonResponse(data, safe=False)