from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import FeesPayments
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    
    return render(request, 'index.html')

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

def login(request):
    if request.method == 'POST':
        ...
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def signup(request):
    return render(request, 'signup.html')


