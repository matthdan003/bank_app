from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime, timedelta
from re import compile as re_compile


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

    def validate_register(self, postData):
        errors = {}
        EMAIL_REGEX = re_compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+.[a-zA-Z]+$'
        )

        # Email validation
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address'
        elif len(self.filter(email=postData['email'])) > 0:
            errors['email'] = 'User with that email already exists'

        # First and last naame validations
        if len(postData['first_name']) < 4:
            errors['first_name'] = 'First name must be 4 or more characters'
        elif len(postData['first_name']) > 45:
            errors['first_name'] = 'First name must be 45 or less characters'
        if len(postData['last_name']) < 4:
            errors['last_name'] = 'Last name must be 4 or more characters'
        elif len(postData['first_name']) > 45:
            errors['last_name'] = 'Last name must be 45 or less characters'

        # Birthdate validation
        todaysDate = datetime.now().date()
        if todaysDate < postData['birthday']:
            errors['birthday'] = 'Birthday must be in the past'
        elif todaysDate - postData['birthday'] < timedelta(days=365*18):
            errors['birthday'] = 'Must be 18 years old to create an account'

        # Password validations
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be 8 opr more characters'
        elif(postData['password'] != postData['password_confirm']):
            errors['password'] = 'Passwords must match'

        return errors


class User(AbstractBaseUser):
    '''Custom user model supporting using email instead of username'''
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
