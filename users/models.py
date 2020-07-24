from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        '''Create and saves a new user'''
        if not email:
            raise ValueError('User must have an email address')
        if not password:
            raise ValueError('User needs a password')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):
    '''Custom user model supporting using email instead of username'''
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
