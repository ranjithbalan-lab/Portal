# D:\Traversy\portal\tickets\views.py
from django.shortcuts import render, redirect,get_object_or_404
from .models import Tickets 
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone
from datetime import datetime
from .models import TICKET_CATEGORY_CHOICES, TICKET_TYPE_CHOICES, TICKET_PRIORITY_CHOICES,TICKET_STATUS,TICKET_ALLOCATED_PERSON 

def index(request):
    # Fetch all tickets
    all_tickets = Tickets.objects.all().order_by('-tk_created_at') 
    
    # Use the context key 'tickets' to match the template loop
    context = {'tickets': all_tickets}
    
    # Return the namespaced template
    return render(request, 'tickets/index.html', context)



def create(request):
    # This is the crucial step: passing the choices lists to the template context
    context = {
        'title': 'Raise a New Ticket',
        # These variables are now correctly defined because they were imported above
        'TICKET_CATEGORY_CHOICES': TICKET_CATEGORY_CHOICES,
        'TICKET_TYPE_CHOICES': TICKET_TYPE_CHOICES,
        'TICKET_PRIORITY_CHOICES': TICKET_PRIORITY_CHOICES,
        # Other context data if needed
    }

    # If handling POST data (form submission) you would do that here.
    if request.method == 'POST':
        # Processing logic for form submission...
        pass
        
    return render(request, 'tickets/create.html', context)

def store(request):
    if request.method == 'POST':
        # 1. Extract data from the POST request
        # Note: If using a Django ModelForm, this is much simpler.
        tk_category = request.POST.get('tk_category')
        tk_type = request.POST.get('tk_type')
        tk_priority = request.POST.get('tk_priority')
        tk_req_by = request.POST.get('tk_req_by')
        tk_req_phone = request.POST.get('tk_req_phone')
        tk_req_email = request.POST.get('tk_req_email')
        tk_unit = request.POST.get('tk_unit')
        tk_menu = request.POST.get('tk_menu')
        tk_due_date = request.POST.get('tk_due_date') or None # Handle empty date
        tk_subject = request.POST.get('tk_subject')
        tk_description = request.POST.get('tk_description')

        try:
            # 2. Create the Ticket instance
            Tickets.objects.create(
                tk_category=tk_category,
                tk_type=tk_type,
                tk_priority=tk_priority,
                tk_req_by=tk_req_by,
                tk_req_phone=tk_req_phone,
                tk_req_email=tk_req_email,
                tk_unit=tk_unit,
                tk_menu=tk_menu,
                tk_due_date=tk_due_date,
                tk_subject=tk_subject,
                tk_description=tk_description,
                # status='Open' # Assuming you have a default status
            )
            
            # 3. Add success message
            messages.success(request, "Ticket submitted successfully!")
            return redirect('tickets:home')

        except Exception as e:
            # Handle potential errors (e.g., database issues)
            messages.error(request, f"Error submitting ticket: {e}")
            return redirect('tickets:create') # Redirect back to form

    # If the request is GET, just redirect to the creation page
    return redirect('tickets:index')

def edit(request, id):
    # Fetch the specific ticket
    ticket_data = get_object_or_404(Tickets, tk_id=id)
    
    # The key in this dictionary MUST match the variable name in your HTML
    context = {
        'ticket': ticket_data,  # Changed from 'tickets' to 'ticket'
        'TICKET_CATEGORY_CHOICES': TICKET_CATEGORY_CHOICES,
        'TICKET_TYPE_CHOICES': TICKET_TYPE_CHOICES,
        'TICKET_PRIORITY_CHOICES': TICKET_PRIORITY_CHOICES,
        'TICKET_STATUS': TICKET_STATUS,
        'TICKET_ALLOCATED_PERSON': TICKET_ALLOCATED_PERSON,
    }
    
    return render(request, 'tickets/edit.html', context)

def update(request, id):
    if request.method == 'POST':
        ticket = get_object_or_404(Tickets, tk_id=id)
        
        try:
            # 1. Update basic text fields
            ticket.tk_category = request.POST.get('tk_category')
            ticket.tk_type = request.POST.get('tk_type')
            ticket.tk_priority = request.POST.get('tk_priority')
            ticket.tk_req_by = request.POST.get('tk_req_by')
            ticket.tk_req_phone = request.POST.get('tk_req_phone')
            ticket.tk_req_email = request.POST.get('tk_req_email')
            ticket.tk_unit = request.POST.get('tk_unit')
            ticket.tk_subject = request.POST.get('tk_subject')
            ticket.tk_description = request.POST.get('tk_description')
            
            # 2. Map dropdowns correctly
            ticket.tk_status = request.POST.get('tk_status')          # Matches 'P'
            ticket.tk_assigned = request.POST.get('tk_assigned_to')  # Matches 'KRB'

            ticket.tk_root_cause = request.POST.get('tk_root_cause')
            ticket.tk_preventive_action = request.POST.get('tk_preventive_action')
            ticket.tk_corrective_action = request.POST.get('tk_corrective_action')

            # 3. FIX: Convert the date string to a timezone-aware object
            due_date_str = request.POST.get('tk_due_date')
            if due_date_str:
                # Convert "2025-12-19" to a datetime object
                naive_date = datetime.strptime(due_date_str, '%Y-%m-%d')
                # Make it aware to satisfy Django's USE_TZ = True
                ticket.tk_due_date = timezone.make_aware(naive_date)
            else:
                ticket.tk_due_date = None

            # 4. Save
            ticket.save()
            
            messages.success(request, f"Ticket #{id} updated successfully.")
            return redirect('tickets:home') # This should now go to list view

        except Exception as e:
            # This is why you are seeing the edit page again
            messages.error(request, f"Update failed: {str(e)}")
            return redirect('tickets:edit', id=id)

    return redirect('tickets:home')