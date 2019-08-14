from django.shortcuts import render
from django.http import HttpResponse
from .models import Museum  #models에 정의된 Museum을 import

def index(request):
    return render(request, 'main/index.html')