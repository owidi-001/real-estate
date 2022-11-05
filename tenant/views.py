from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user.models import UserType


# Tenant dashboard
def tenant_dashboard(request):
    if request.user.is_authenticated and UserType.objects.get(user=request.user).is_tenant:
        bucket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        return render(request, 'dashboard/tenant/tenant_dashboard.html', {'bucket': bucket})
    else:
        messages.info(request, "Login required for this")
        return redirect('login')
