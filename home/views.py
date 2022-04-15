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
        context["entry"] = ""
        context["nav1"] = "Student Login"
        context["link1"] = "login"
        context["nav2"] = "Sign Up"
        context["link2"] = "signup"
        

    else:
        context = {"message": f"You are logged in as {request.user.username}"}
        context["entry"] = request.user.username
        context["nav1"] = "Pay Fees"
        context["link1"] = "payfees"
        context["nav2"] = f"Logout ({request.user.username})"
        context["link2"] = "logout"
    return render(request, 'index.html', context)

def auth(request):
    return HttpResponse("You're at the home auth.")

def dashboard(request):
    if request.user.is_anonymous:
        context = {"entry": ""}
        context["nav1"] = "Student Login"
        context["link1"] = "login"
        context["nav2"] = "Sign Up"
        context["link2"] = "signup"

    else:
        context = {"entry": request.user.username}
        context["nav1"] = "Pay Fees"
        context["link1"] = "payfees"
        context["nav2"] = f"Logout ({request.user.username})"
        context["link2"] = "logout"
        for sem in range(1, 9):
            obj = FeesPayments.objects.filter(entry=request.user.username ,semester=sem)
            if obj:
                context[f"sem{sem}"] = "Paid"
            else:
                context[sem] = ""

    return render(request, 'dashboard.html', context)

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
        return redirect('/dashboard')


    if request.user.is_anonymous:
        context = {"entry": ""}
        context["nav1"] = "Student Login"
        context["link1"] = "login"
        context["nav2"] = "Sign Up"
        context["link2"] = "signup"

    else:
        context = {"entry": request.user.username}
        context["nav1"] = "Pay Fees"
        context["link1"] = "payfees"
        context["nav2"] = f"Logout ({request.user.username})"
        context["link2"] = "logout"
        for sem in range(1, 9):
            obj = FeesPayments.objects.filter(entry=request.user.username ,semester=sem)
            if obj:
                context[f"sem{sem}"] = "Paid"
            else:
                context[sem] = ""
    
    return render(request, 'payfees.html', context)

    

def status(request):
    return HttpResponse("You're at the home status.")

def loginuser(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        print(username, password)
        try:
            user = User.objects.get(username=username)
        except:
            # return HttpResponse("This entry no. doesn't exists")
            context["error"] = "This entry no. does not exists"
        else:
            user = User.objects.filter(username=username, password=password)
            user = authenticate(username=username, password=password)
            if user:
                print("user is logged in")
                login(request, user)
                return redirect('/dashboard')
            
            else:
                print("user is not logged in")
                # return HttpResponse("Invalid login details supplied.")
                context["error"] = "Invalid login details supplied."
        

    if request.user.is_anonymous:
        context["message"] = "You are not logged in"
        context["entry"] = ""
        context["nav1"] = "Student Login"
        context["link1"] = "login"
        context["nav2"] = "Sign Up"
        context["link2"] = "signup"
        

    else:
        context["message"] = f"You are logged in as {request.user.username}"
        context["entry"] = request.user.username
        context["nav1"] = "Pay Fees"
        context["link1"] = "payfees"
        context["nav2"] = f"Logout ({request.user.username})"
        context["link2"] = "logout"
    
    context["flip"] = "true"
    return render(request, 'signup.html', context)

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

        try:
            user = User.objects.get(username=username)
        except:
            user = User.objects.create_user(username=username, password=raw_password)
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/dashboard')
        
        print("this entry no. is already taken")
        context = {"error": "You have already created an account. Please try logging in again or contact the administrator."}
        return render(request, 'signup.html', context)


    if request.user.is_anonymous:
        context = {"message": "You are not logged in"}
        context["entry"] = ""
        context["nav1"] = "Student Login"
        context["link1"] = "login"
        context["nav2"] = "Sign Up"
        context["link2"] = "signup"
        

    else:
        context = {"message": f"You are logged in as {request.user.username}"}
        context["entry"] = request.user.username
        context["nav1"] = "Pay Fees"
        context["link1"] = "payfees"
        context["nav2"] = f"Logout ({request.user.username})"
        context["link2"] = "logout"
    
    context["flip"] = ""
    return render(request, 'signup.html', context)


