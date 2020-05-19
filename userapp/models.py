from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

"""
Solution followed from django docs
https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#a-full-example
"""

class MyUserManager(BaseUserManager):
    def create_user(self, username, display_name, password, homepage, age):
        if not username:
            raise ValueError('User must have a username')
        if not display_name:
            display_name = username
        if not homepage:
            homepage = "https://customuserappthing.com/" + username
        if not age:
            age = 0
        user = self.model(
            username=username,
            display_name=display_name,
            homepage=homepage,
            age=age
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, password, display_name=None, homepage=None, age=None):
        user = self.create_user(
            username,
            display_name,
            password,
            homepage,
            age
        )
        user.is_admin = True
        user.save(using=self.db)
        return user

class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    display_name = models.CharField(max_length=30)
    homepage = models.URLField(null=True)
    age = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = MyUserManager()
    
    USERNAME_FIELD = 'username'
    # Found solution here in line 54 of the source for createsuperuser
    # https://github.com/django/django/blob/master/django/contrib/auth/management/commands/createsuperuser.py
    REQUIRED_FIELDS = ['age']
    
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin