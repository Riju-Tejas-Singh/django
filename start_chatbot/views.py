from django.shortcuts import render
from django.http import HttpResponse

def chatbot_start(request):
    return HttpResponse("Chatbot Started!")
