from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user.models import UserType


# Tenant dashboard
# @login_required
def tenant_dashboard(request):
    if request.user.is_authenticated and UserType.objects.get(user=request.user).is_tenant:
        return render(request, 'tenant/tenant_dashboard.html')
    else:
        messages.info(request, "Login required for this")
        return redirect('login')
