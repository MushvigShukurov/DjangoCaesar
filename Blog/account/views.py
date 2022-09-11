
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as l,logout as lt
from .caesar import Caesar
from django.utils import timezone
indikiVaxt = timezone.now().year
# Create your views here.
def index(request):
    
    if request.method == "POST":
        if "des" in request.POST:
            if not request.user.is_authenticated:
                return redirect("login")
            cryptText = request.POST["sifreliMetnname"]
            text = Caesar(cryptText,703,True)
            data = {
                "sifreliMetn":cryptText,
                "metn":text,
                "time":indikiVaxt
            }
        else:
            text = request.POST["sifrelenecekMetn"]
            # cryptText = f.encrypt(text.encode())
            cryptText = Caesar(text,703,False)
            data = {
                "text":text,
                "crypt":cryptText,
                "time":indikiVaxt
            }
        return render(request,"index.html",data)
    data = {
        "time":indikiVaxt
    }
    return render(request,"index.html",data)


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password) 
        if user is not None:
            l(request,user)
            return redirect("home")
        else:
            return redirect("login")
    data = {
        "time":indikiVaxt
    }
    return render(request,"login.html",data)

def registration(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        if password == repassword:
            if not User.objects.filter(username = username).exists():
                user = User.objects.create_user(username = username,password = password)
                user.save()
                return redirect("login")
        else:
            return render(request,"registration.html",{"username" : username})
    data = {
        "time":indikiVaxt
    }
    return render(request,"registration.html",data)


def logout(request):
    lt(request)
    return redirect("login")


