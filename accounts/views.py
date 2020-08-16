from django.shortcuts import render, redirect,reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm

# Create your views here.
def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')

def logout(request):
    """log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfuly been logged out")
    return redirect(reverse('index'))

def login(request):
    """return a login page"""
    #auth.login(request)
    if request.method == "POST":
         login_form=UserLoginForm(request.POST)
         if login_form.is_valid():
             user=auth.authenticate(username=request.POST['username'],
             password=request.POST['password'])
             if user:
                 auth.login(user=user, request=request)
                 messages.success(request, "Logged in!")
             else:
                login_form.add_error(None, "your username or password is incorrect")
    else:
        login_form =UserLoginForm()
    return render(request, 'login.html', {"login_form":login_form})