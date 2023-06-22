# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import UserCreationForm
from .models import User, UserType


# register
def signup(request):
    form = UserCreationForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        is_landlord = False
        is_tenant = False
        is_agent = False

        if user_type == "is_landlord":
            is_landlord = True
        elif user_type == "is_agent":
            is_agent = True
        else:
            is_tenant = True

        user = User.objects.create_user(
            email=email, phone=phone
        )
        user.set_password(password)
        user.save()

        if is_landlord:
            user_type = UserType(user=user, is_landlord=True)
            user_type.save()
        elif is_agent:
            user_type = UserType(user=user, is_agent=True)
            user_type.save()
        elif is_tenant:
            user_type = UserType(user=user, is_tenant=True)
            user_type.save()

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            type_obj = UserType.objects.get(user=user)
            if user.is_authenticated and type_obj.is_landlord:
                return redirect('landlord_dashboard')  # Go to landlord dashboard
            elif user.is_authenticated and type_obj.is_tenant:
                return redirect('tenant_dashboard')  # Go to tenant dashboard
            elif user.is_authenticated and type_obj.is_agent:
                return redirect('agent_dashboard')  # Go to agent dashboard

    # if form.errors:
    #     messages.error(request, form.errors)

    return render(request, 'auth/register.html')


# login
def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email value from form
        password = request.POST.get('password')  # Get password value from form

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            type_obj = UserType.objects.get(user=user)
            if user.is_authenticated and type_obj.is_landlord:
                return redirect('landlord_dashboard')  # Go to landlord dashboard
            elif user.is_authenticated and type_obj.is_tenant:
                return redirect('tenant_dashboard')  # Go to tenant dashboard
            elif user.is_authenticated and type_obj.is_agent:
                return redirect('agent_dashboard')  # Go to agent dashboard
        else:
            # Invalid email or password. Handle as you wish
            return redirect('home')

    return render(request, 'auth/login.html')


# Home view
def home(request):
    return render(request, "home/home.html")

# logout

# DONE: on urls

# profile

# profile edit
