from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("You're are looking at polls index" )

def details(request, question_id):
    return HttpResponse("You're are looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of the question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)