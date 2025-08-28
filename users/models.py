from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.conf import settings

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, phone_number=None, password=None, **extra_fields):
        if not username:
            raise ValueError("A user must have a username")
        if not email and not phone_number:
            raise ValueError("A user must have either an email or phone number")

        if email:
            email = self.normalize_email(email)

        user = self.model(
            username=username,
            email=email,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField( null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='Profile')
    photo=models.ImageField(upload_to='profile_pics/',null=True,blank=True)
    bio =models.TextField(blank=True,null=True)

    def __str__(self):
     return f"{self.user.username}'Profile"