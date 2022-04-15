from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import FeesPayments
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        context = {"message": "You are not logged in"}
    else:
        context = {"message": "You are logged in"}
    return render(request, 'index.html', context)

def auth(request):
    return HttpResponse("You're at the home auth.")

def dashboard(request):
    return render(request, 'dashboard.html')
    # return HttpResponse("You're at the home dashboard.")

def payfees(request):
    if request.method == 'POST':
        print("post")
        name = request.POST.get('fname')
        entry = request.POST.get('entry')
        semester = request.POST.get('semester')
        # amount = request.POST.get('amount')
        amount = 100000 + 5000*int(semester)
        date = datetime.now().date()
        time = datetime.now().time()
        feespayments = FeesPayments(name=name, entry=entry, semester=semester, amount=amount, date=date, time=time)
        feespayments.save()



    return render(request, 'payfees.html')

def status(request):
    return HttpResponse("You're at the home status.")

def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        user = User.objects.filter(username=username, password=password)
        print(username, password)

        if user is not None:
            print("user is logged in")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/payfees')
        else:
            print("user is not logged in")
            login(request, user)
            return render(request, 'login.html')
        

    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        raw_password = request.POST.get('psw')
        print("post")

        # if form.is_valid():
        # print("form is valid")
        # form.save()
        # username = form.cleaned_data.get('username')
        # raw_password = form.cleaned_data.get('password1')
        print(username, raw_password)
        user = User.objects.create_user(username=username, password=raw_password)
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('/payfees')

    return render(request, 'signup.html')


