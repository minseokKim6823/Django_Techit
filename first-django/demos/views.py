from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def calculator(request):
    return HttpResponse("계산기 기능 구현")