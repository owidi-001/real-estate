from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user.models import UserType


# Tenant dashboard
def landlord_dashboard(request):
    if request.user.is_authenticated and UserType.objects.get(user=request.user).is_landlord:
        return render(request, 'dashboard/landlord/landlord_dashboard.html')
    else:
        return redirect('login')
