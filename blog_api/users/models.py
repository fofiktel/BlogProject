from django.contrib.auth.hashers import make_password
from django.db import models, transaction
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, nickname, password=None, **extra_fields):

        user = self.model(email=self.normalize_email(email), nickname=nickname)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, nickname, password, **extra_fields):

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, nickname, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=40, unique=True)
    nickname = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email', ]

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    def __str__(self):
        return self.nickname


class Country(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Rang(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


def create_path(instance, filename):
    return f'images/profile_avatar/profile_{instance.pk}_avatar.jpg'


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, primary_key=True)
    profile_image = models.ImageField(upload_to=create_path,
                                      default='images/profile_avatar/default_avatar.jpg')

    join_date = models.DateField(default=timezone.now)
    self_information = models.TextField(default='', blank=True)
    origin_country = models.ForeignKey(Country, related_name='origin_country', on_delete=models.PROTECT, null=True, blank=True)
    rang = models.ForeignKey(Rang, related_name='rang', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.user.nickname

