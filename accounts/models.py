from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Products

# Create your models here.


class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='profiles/', blank=True)
    like = models.ManyToManyField(Products, related_name='like')
    followers = models.ManyToManyField(
        'self', symmetrical=False, related_name='following', blank=True)

    def follow(self, user):
        if user not in self.following.all():
            self.following.add(user)

    def unfollow(self, user):
        if user in self.following.all():
            self.following.remove(user)

    def is_following(self, user):
        return user in self.following.all()

    def get_followers(self):
        return self.followers.all()

    def get_following(self):
        return self.following.all()
