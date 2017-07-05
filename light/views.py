from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.
# CURRENT USER
def current_user(request):
    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])
# INDEX ROUTE
def index(request):
    return render(request, 'light/index.html')
# END INDEX
# PROCESS
def process(request):
    is_valid = User.objects.register_validate(request.POST)
    if is_valid['errors']:
        for error in is_valid['errors']:
            messages.error(request, error)
        return redirect('/#light')
    else:
        # user = User.objects.create_user(request.POST)
        # request.session['user_id'] = user.id
        return redirect('/home')
# LOGIN
def login(request):
    is_valid = User.objects.login_validate(request.POST)
    if is_valid['status'] == True:
        request.session['user.id'] = is_valid['user'].id
        return redirect('/home')
    else:
        if is_valid['status'] == False:
            messages.error(request, is_valid['message'])
            return redirect('/')
# LOGOUT
def logout(request):
    request.session.clear()
    return redirect('/')
# HOME
def home(request):
    return render(request, 'light/home.html')
# END HOME
