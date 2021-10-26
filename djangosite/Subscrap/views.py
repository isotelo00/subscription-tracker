from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader

from .forms import *

def home(request):
	return render(request, 'subscrap/home.html')

def createSub(request):
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = addForm(request.POST)

		print(form.errors)
		if form.is_valid():
            # todo: save to db and link to user
			print(form.cleaned_data["sub_name"])
			print(form.cleaned_data["sub_price"])
			print(form.cleaned_data["sub_date"])
            # redirect to a new URL:
			return HttpResponseRedirect('/create/')

    # if a GET (or any other method) we'll create a blank form
	else:
		form = addForm()

	return render(request, 'subscrap/create.html', {'form': form})

# def login(request):
#  return HttpResponse(request, 'subscrap/Login.html')


# def signup(request):
#   return HttpResponse(request, 'subscrap/Signup.html')
