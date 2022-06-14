from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta número {question_id}.")

def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta número {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"Estas votando en la pregunta número {question_id}.")
