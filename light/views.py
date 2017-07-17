from django.shortcuts import render, redirect
from django.db.models import Count
from .models import *
from django.contrib import messages
# Create your views here.
# CURRENT USER
def current_user(request):
    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])
# INDEX ROUTE
def index(request):
    if current_user(request):
        return redirect('/home')
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
        user = User.objects.create_user(request.POST)
        request.session['user_id'] = user.id
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
def logout(request  ):
    request.session.clear()
    return redirect('/')
# HOME
def home(request):
    if 'user_id' in request.session:
        user = current_user(request)

        context = {
        'current_user': user
        }

        return render(request, 'light/home.html', context)
    return redirect('/')
# END HOME
# REVIEWS
def reviews(request):
    if not current_user:
        return redirect('/')
    user = current_user(request)
    popular_reviews = Review.objects.annotate(num_likes=Count('liked_by')).order_by('-num_likes')[:3]
    context = {
    'current_user': user,
    'reviews': Review.objects.all().order_by('-created_at'),
    'popular_reviews': popular_reviews,
    }
    return render(request, 'light/reviews.html', context)
# CREATE REVIEWS
def create_review(request):
    user = current_user(request)
    review = Review.objects.create_review(request.POST, user)
    return redirect('/reviews')
# LIKE REVIEWS
def like(request, id):
    user = current_user(request)
    review = Review.objects.get(id=id)
    review.liked_by.add(user.id)
    return redirect('/reviews')
def unlike(request, id):
    user = current_user(request)
    review = Review.objects.get(id=id)
    review.liked_by.remove(user.id)
    return redirect('/reviews')
# ACCOUNT
def account(request, id):
    user = current_user(request)
    reviews = Review.objects.filter(id=user.id)
    context = {
        'current_user': user,
        'reviews': reviews,
    }
    return render(request, 'light/account.html', context)
# DELETE
def delete(request, id):
    user = current_user(request)
    user.delete()
    return redirect('/')
