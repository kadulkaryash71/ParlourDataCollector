from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib import messages
from django.http import HttpResponse
from .models import *

# Create your views here.

# Service Views
class ServiceCreateView(CreateView):
    
    model = Service
    fields = '__all__' 
    template_name = 'service/create_service.html'

    def queryset(self):
        pass

    def post(self, request, *args, **kwargs):
        name = request.POST.get('service-name')
        rate = request.POST.get('service-rate')

        try:
            Service.objects.create(service_name=name.capitalize(), rate=int(rate))
            messages.success(request, "Hurray! Item created.")
        except Exception as e:
            print('Error occured:', e)
            messages.error(request, "Item couldn't be added in the database. Try again!")

        return redirect('add_service')

# Transaction Views
class TransactionCreateView(CreateView):
    
    model = Transaction
    fields = '__all__'
    template_name = 'transaction/create_transaction.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def post():
        pass
    

# Function-based views
def index(request):
    return render(request, 'base.html')