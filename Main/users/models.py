from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


# Custom user profile that has been extended from django AbstractUser
class Profile(AbstractUser):
    class UserType(models.TextChoices):
        TEACHER = '1', 'Teacher'
        STUDENT = '2', 'Student'
    user_type = models.CharField(max_length=20, choices=UserType.choices, default=UserType.STUDENT)
    university = models.CharField(max_length=50)
    
