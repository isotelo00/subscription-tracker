from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(request):
    # return HttpResponse('<h1> Home</h1>')
    return render(request, 'subscrap/home.html')


# def login(request):
  #  return HttpResponse(request, 'subscrap/Login.html')


# def signup(request):
 #   return HttpResponse(request, 'subscrap/Signup.html')
