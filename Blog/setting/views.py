from django.shortcuts import render
from .models import SiteSettings
# Create your views here.

def index(request):
    about = SiteSettings.objects.first()
    data = about
    return render(request,"about.html",{"setting":data})