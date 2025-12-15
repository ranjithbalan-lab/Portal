from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee

# Create your views here.

def index(request):
    employees = Employee.objects.all()
    return render(request,'index.html',{'employees':employees})

def create(request):
    return render(request,'create.html')

def store(request):
    if request.method == 'POST':
        # 1. Retrieve data from the POST request
        emp_name = request.POST.get('emp_name')
        emp_email = request.POST.get('emp_email')
        emp_phone = request.POST.get('emp_phone')
        emp_dept = request.POST.get('emp_dept')
        emp_unit = request.POST.get('emp_unit')
        emp_designation = request.POST.get('emp_designation')
        emp_manager = request.POST.get('emp_manager')
        emp_status = request.POST.get('emp_status')
        emp_dob = request.POST.get('emp_dob')
        emp_doj = request.POST.get('emp_doj')
        emp_dor = request.POST.get('emp_dor') # Optional field

        # 2. Create and save the new Employee object
        Employee.objects.create(
            emp_name=emp_name,
            emp_email=emp_email,
            emp_phone=emp_phone,
            emp_dept=emp_dept,
            emp_unit=emp_unit,
            emp_desgination=emp_designation,
            emp_manager=emp_manager,
            emp_status=emp_status,
            emp_dob=emp_dob,
            emp_doj=emp_doj,
            emp_dor=emp_dor if emp_dor else None # Handle empty date field
        )

        # 3. SUCCESS PATH: Redirect the user back to the home/list page
        return redirect('home') # 'home' is the URL name for your employee list

    # 4. ERROR PATH/FALLBACK: If the request is NOT POST (i.e., GET request),
    #    redirect the user to the form page or the list page, as this view
    #    shouldn't typically be accessed directly via GET.
    #    In this case, redirecting to the actual form page is safest.
    return redirect('store') # 'create_view' is the URL name for the form itself

def edit(request, id):
    emp = get_object_or_404(Employee, emp_id=id)
    return render(request, 'edit.html', {'emp': emp})

def update(request, id):
    emp = get_object_or_404(Employee, emp_id=id)

    if request.method == 'POST':
        emp.emp_name = request.POST.get('emp_name')
        emp.emp_email = request.POST.get('emp_email')
        emp.emp_phone = request.POST.get('emp_phone')
        emp.emp_dept = request.POST.get('emp_dept')
        emp.emp_unit = request.POST.get('emp_unit')
        emp.emp_desgination = request.POST.get('emp_designation')
        emp.emp_manager = request.POST.get('emp_manager')
        emp.emp_status = request.POST.get('emp_status')
        emp.emp_dob = request.POST.get('emp_dob') or None
        emp.emp_doj = request.POST.get('emp_doj')
        emp.emp_dor = request.POST.get('emp_dor') or None

        emp.save()
        return redirect('home')

    return redirect('edit', id=id)

def delete(request, id):
    emp = get_object_or_404(Employee, emp_id=id)
    if request.method == 'POST':
        emp.delete()
        return redirect('home')
