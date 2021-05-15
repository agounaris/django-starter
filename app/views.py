# social_app/views.py

from django.views.generic import TemplateView
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

class Home(TemplateView):
    template_name = "home.html"


def dashboard(request):
    if not request.user.is_authenticated:
        return render(request, '404.html')
    return render(request, 'dashboard.html')
