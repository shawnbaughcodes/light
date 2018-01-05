from django.shortcuts import render, redirect
from django.db.models import Count
from .models import *
from django.contrib import messages
import json
from django.http import HttpResponse, JsonResponse
from django.core import serializers
# Create your views here.
# CURRENT USER
def current_user(request):
    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])
# INDEX ROUTE
def index(request):
    if current_user(request):
        return redirect('/home')
    reviews = Review.objects.all().order_by('-created_at')
    data = serializers.serialize('json', reviews)
    return render(request, 'light/index.html', data)
# END INDEX
# PROCESS
def process(request):
    is_valid = User.objects.register_validate(request.POST)
    if is_valid['errors']:
        for error in is_valid['errors']:
            messages.error(request, error)
        return redirect('/#light')
    else:
        user = User.objects.create_user(request.POST)
        request.session['user_id'] = user.id
        return redirect('/home')
# LOGIN
def login(request):
    is_valid = User.objects.login_validate(request.POST)
    if is_valid['status'] == True:
        request.session['user_id'] = is_valid['user'].id
        return redirect('/home')
    else:
        if is_valid['status'] == False:
            messages.error(request, is_valid['message'])
            return redirect('/home')
# LOGOUT
def logout(request  ):
    request.session.clear()
    return redirect('/')
# HOME
def home(request):
    if 'user_id' in request.session:
        user = current_user(request)
        popular_reviews = Review.objects.annotate(num_likes=Count('liked_by')).order_by('-num_likes')[:3]
        context = {
        'current_user': user,
        'reviews': Review.objects.all().order_by('-created_at'),
        'popular_reviews': popular_reviews,
        'friends': user.friends.all(),
        'friends_ids': user.friends.all().values_list('id', flat=True)
        }
        return JsonResponse(context)
        return render(request, 'light/home.html', context)
    return redirect('/')
# END HOME
# CREATE REVIEWS
def create_review(request):
    user = current_user(request)
    review = Review.objects.create_review(request.POST, user)
    return redirect('/home')
# LIKE REVIEWS
def like(request, id):
    user = current_user(request)
    review = Review.objects.get(id=id)
    review.liked_by.add(user.id)
    return redirect('/home')
def unlike(request, id):
    user = current_user(request)
    review = Review.objects.get(id=id)
    review.liked_by.remove(user.id)
    return redirect('/home')
# ACCOUNT
def account(request, id):
    user = current_user(request)
    reviews = Review.objects.filter(id=user.id)
    context = {
        'current_user': user,
        'reviews': reviews,
    }
    return render(request, 'light/account.html', context)
# DELETE ACCOUNT
def delete(request, id):
    user = current_user(request)
    user.delete()
    return redirect('/')
# ADD FRIEND
def add(request, id):
    user = current_user(request)
    user.friends.add(id)
    return redirect('/home')
def unfriend(request, id):
    user = current_user(request)
    user.friends.remove(id)
    return redirect('/home')
