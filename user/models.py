from django.db import models
from django.utils import timezone
from core.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from address.models import City, District, Ward


class UserManager(BaseUserManager):

    def create_user(self, username, password, email, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        else:
            email = self.normalize_email(email)
        if not username:
            raise ValueError("Username is required")
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, email, **extra_fields)


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.username


class UserAddress(BaseModel):
    user = models.ForeignKey(User, to_field="key", on_delete=models.CASCADE)
    address_line = models.TextField()
    phone = models.CharField(max_length=20)
    city = models.ForeignKey(City, to_field="key", on_delete=models.CASCADE)
    district = models.ForeignKey(District, to_field="key", on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, to_field="key", on_delete=models.CASCADE)

    def __str__(self):
        return self.address_line
