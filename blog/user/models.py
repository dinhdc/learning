from distutils.command.upload import upload
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
  
  def create_user(self, email: str, password=None, **extra_fields):
    if not email:
        raise ValueError(_('The Email must be set'))
    user = self.model(email=email.lower(), **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email: str, password, **extra_fields):
    user = self.create_user(email=email, password=password, **extra_fields)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    fullname = models.CharField(_('full name'), max_length=255)
    phone = models.CharField(_('phone'), max_length=255)
    avatar = models.ImageField(_('avatar'), upload_to="avatars", null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname',]

    objects = CustomUserManager()

    def __str__(self):
        return self.email