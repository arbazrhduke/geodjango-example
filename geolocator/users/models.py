from django.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
class MyUserManager(BaseUserManager):
    def create_user(self,email, password=None):
        """
        Creates and saves a User with the given email,password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email, password):
        """
        Creates and saves a superuser with the given email,username and password.
        """
        user = self.create_user(email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

#Users
class User(AbstractBaseUser):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15,null=True)
    #password = models.CharField(max_length=64)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    is_premium = models.BooleanField(default=False)
    objects = MyUserManager()

class Address_Type(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)

class Address(models.Model):
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=12)
    landmark = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zip = models.IntegerField()
    country = models.CharField(max_length=64,null=True)
    type = models.ForeignKey(Address_Type)
    user = models.ForeignKey(User)

from django.contrib.gis.db import models
class Place(models.Model):
    id = models.IntegerField(primary_key=True)
    location = models.PointField(null=True, blank=True)
    address = models.ForeignKey(Address)
    objects = models.GeoManager()

