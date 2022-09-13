from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user.models import UserType


# agent dashboard
@login_required
def agent_dashboard(request):
    if request.user.is_authenticated and UserType.objects.get(user=request.user).is_agent:
        return render(request, 'agent/agent_dashboard.html')
    else:
        return redirect('login')
