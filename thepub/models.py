from django.contrib.auth.models import User
from django.db import models

"""Shareable"""


class Shareable(models.Model):
    url = models.URLField(max_length=2000)
    created_datetime = models.DateTimeField(auto_now_add=True)
    deleted_datetime = models.DateTimeField(null=True, blank=True)
    labels = models.ManyToManyField('Label', through='ShareableLabel')
    shared_by = models.ForeignKey('UserProfile')

    def __str__(self):
        return "%s shared by %s" % (self.url, self.shared_by.__str__())


class Label(models.Model):
    label_name = models.CharField(max_length=200)


class ShareableLabel(models.Model):
    label = models.ForeignKey(Label)
    shareable = models.ForeignKey(Shareable)
    created_datetime = models.DateTimeField(auto_now_add=True)
    deleted_datetime = models.DateTimeField(null=True, blank=True)


"""User"""


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_test_user = models.BooleanField(default=False)
    is_beta_user = models.BooleanField(default=False)

    def __str__(self):
        return self.user.__str__()



