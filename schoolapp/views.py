from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Department,Course,Order,Material
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

# Create your views here.
def home(request):
     departments = Department.objects.all()
     return render(request, 'index.html', {'departments': departments})
    
def department_detail(request, department_id):
    department = Department.objects.get(pk=department_id)
    courses = Course.objects.all()
    return render(request, 'department_detail.html', {'department': department, 'courses': courses})
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        if password == confirmPassword:
            if User.objects.filter(username=username).exists() :
                messages.error(request, "Username  already in use")
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "User Created.")
                return redirect("home")
        else:
            messages.error(request, "Password not matching")

        return redirect('register')

    return render(request, 'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate( username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login successful.")
            return redirect('staff') 

        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')

    return render(request, 'login.html')





def logout(request):
    auth.logout(request)
    return redirect('home')


def staff(request):
    if request.method == 'POST':
       
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department_id = request.POST.get('department')
        course_id = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials_provided_names = request.POST.getlist('materials[]')

       
        materials_provided_objects = Material.objects.filter(name__in=materials_provided_names)

        order = Order(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone_number,
            email=email,
            address=address,
            department_id=department_id,
            course_id=course_id,
            purpose=purpose
        )
        order.save()

        if materials_provided_objects.count() == len(materials_provided_names):
          
            materials_provided_ids = materials_provided_objects.values_list('id', flat=True)
            order.materials_provided.set(materials_provided_ids)

           
            return render(request, 'order_confirm.html')
        else:
            
            
            return render(request, 'order_confirm.html', {'departments': Department.objects.all()})

    return render(request, 'staff.html', {'departments': Department.objects.all()})




def order_confirm(request):
  return render(request, 'order_confirm.html')



# def staff(request):
#     departments = Department.objects.all()
#     purposes = ['For Enquiry', 'Place Order', 'Return']  # Add your purposes as needed

#     context = {
#         'departments': departments,
#         'purposes': purposes,
#     }

#     return render(request, 'staff.html', context)

def get_courses(request):
    department_id = request.GET.get('department_id', None)

    if department_id is not None:
        courses = Course.objects.filter(department_id=department_id)
        course_data = [{'id': course.id, 'name': course.name} for course in courses]
        return JsonResponse(course_data, safe=False)
         
    return JsonResponse([], safe=False)