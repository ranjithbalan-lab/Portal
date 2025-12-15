# D:\Traversy\portal\tickets\views.py

from django.shortcuts import render
from .models import Tickets 

def index(request):
    # Fetch all tickets
    all_tickets = Tickets.objects.all().order_by('-tk_created_at') 
    
    # Use the context key 'tickets' to match the template loop
    context = {'tickets': all_tickets}
    
    # Return the namespaced template
    return render(request, 'tickets/index.html', context)

def create(request):
    return render(request,'tickets/create.html')