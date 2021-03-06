from __future__ import unicode_literals

from django.db import models
import re, bcrypt

# Create your models here.
# USER MANAGER
class UserManager(models.Manager):
    def register_validate(self, post):
        result = {'errors': []}
        if len(post['name']) < 2:
            result['errors'].append('Invalid name.')
        if not re.search(r'\w+\@\w+\.\w+', post.get('email')):
            result['errors'].append('Invalid email.')
        if len(post['password']) < 4:
            result['errors'].append('Invalid password')
        if post['password_confirmation'] != post['password']:
            result['errors'].append('Invalid Confirmation')
        return result
    # END REGISTER VALIDATE
    def create_user(self, post):
        user = User.objects.create(name=post.get('name'), email=post.get('email'), password=bcrypt.hashpw(post.get('password').encode(), bcrypt.gensalt()))
        return user
        #  END CREATE USER
    def login_validate(self, post):
        user = User.objects.filter(email=post.get('email')).first()
        if user and bcrypt.hashpw(post.get('password').encode(), user.password.encode()) == user.password:
            return {'status': True, 'user': user}
        else:
            return {'status': False, 'message': 'Invalid credentials.'}
        # END LOGIN VALIDATE
    def login(self, request, user):
        if('user_id' not in request.session):
            request.session['user_id': user.id]
    # END LOGIN
# END USER MANAGER
# REVIEWS MANAGER
class ReviewManager(models.Manager):
    def create_review(self, post, user):
        review = Review.objects.create(media=post.get('media'), topic=post.get('topic'), location=post.get('location'), artist=post.get('artist'), content=post.get('content'), user=user)
        return review
#END REVIEWS MANAGER
# USER MODEL
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=300)
    friends = models.ManyToManyField('self')
    password = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
# REVIEWS MODEL
class Review(models.Model):
    topic = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    media = models.FileField(default='')
    content = models.CharField(max_length=1000)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
