from django.contrib.auth.models import User
from django.db import models

"""Shareable"""


class Url(models.Model):
    url = models.URLField(max_length=2000, unique=True)


class Shareable(models.Model):
    url = models.ForeignKey(Url)
    created_datetime = models.DateTimeField(auto_now_add=True)
    deleted_datetime = models.DateTimeField()
    labels = models.ManyToManyField(Label, through='ShareableLabel')
    shared_by = models.ForeignKey(UserProfile)


class Label(models.Model):
    label_name = models.CharField(max_length=200)


class ShareableLabel(models.Model):
    label = models.ForeignKey(Label)
    shareable = models.ForeignKey(Shareable)
    created_datetime = models.DateTimeField(auto_now_add=True)
    deleted_datetime = models.DateTimeField()


"""User"""


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    invited_by = models.ForeignKey("self")
    is_test_user = models.BooleanField(default=False)




