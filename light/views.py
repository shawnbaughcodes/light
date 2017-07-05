from django.shortcuts import render, redirect
from .models import *
# Create your views here.
# INDEX ROUTE
def index(request):
    return render(request, 'light/index.html')
# END INDEX
