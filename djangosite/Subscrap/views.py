from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.views.generic import ListView, DetailView, CreateView
from .models import SubscriptionList, SubscriptionItem

from Subscrap.models import SubscriptionItem

from .forms import *


def home(request):
    return render(request, 'subscrap/home.html')


def testMain(request):
    context = {
        'items': SubscriptionItem.objects.all()
    }
    return render(request, 'subscrap/testMain.html', context)


def createSub(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = addForm(request.POST)

		print(form.errors)
		if form.is_valid():
			# todo: save to db and link to user
			name=form.cleaned_data["sub_name"]
			price=form.cleaned_data["sub_price"]
			start=form.cleaned_data["sub_date"]
			end=form.cleaned_data["sub_exp"]
			print(name)
			print(price)
			print(start)
			sub = SubscriptionItem(name=name, price=price, startDate=start, expirationDate=end, postitionInList=SubscriptionItem.objects.count())
			sub.save()
            # redirect to a new URL:
			return HttpResponseRedirect('/create/')

    # if a GET (or any other method) we'll create a blank form
	else:
		form = addForm()

	return render(request, 'subscrap/create.html', {'form': form})

def editSub(request):
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = editForm(request.POST)

		print(form.errors)
		if form.is_valid():
            # todo: save to db and link to user
			name=form.cleaned_data["sub_name"]
			price=form.cleaned_data["sub_price"]
			start=form.cleaned_data["sub_date"]
			print(name)
			print(price)
			print(start)
			#sub = SubscriptionItem(name=name, price=price, startDate=start)
			#sub.save()
            # redirect to a new URL:
			return HttpResponseRedirect('/edit/')

    # if a GET (or any other method) we'll create a blank form
	else:
		form = editForm()

	return render(request, 'subscrap/edit.html', {'form': form})

# def login(request):
#  return HttpResponse(request, 'subscrap/Login.html')


# def signup(request):
#   return HttpResponse(request, 'subscrap/Signup.html')

class SubscriptionPostView(ListView):
    model = SubscriptionItem
    template_name = 'Subscrap/testMain.html'
    context_object_name = 'items'
    ordering = ['startDate']


class SubscriptionDetailView(DetailView):
    model = SubscriptionItem
    template_name = 'Subscrap/subscriptionDetails.html'


class SubscriptionCreateView(CreateView):
    model = SubscriptionItem
    fields = ['name', 'price', 'cyclePeriod',
              'expirationDate', 'muted', 'SubscriptionList']
    template_name = 'Subscrap/createSubscription.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid
