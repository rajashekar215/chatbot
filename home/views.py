# =============================================================================
# from django.shortcuts import render
# 
# # Create your views here.
# def hello(request):
#    return render(request, "home/templates/home.html", {})
# 
# 
# =============================================================================
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "home/home.html", {'x':"welcome to chatbot"})
