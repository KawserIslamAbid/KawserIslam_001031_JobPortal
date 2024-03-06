from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_User(AbstractUser):
    USER_TYPE = (
        ('Admin', 'Admin'),
        ('Job Seeker', 'Job Seeker'),
        ('Recruiter', 'Recruiter'),
    )
    display_name = models.CharField(max_length=50)
    user_type = models.CharField(max_length=20, choices=USER_TYPE, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.user_type == 'Recruiter' and not hasattr(self, 'user_company'):
            Company.objects.create(user=self, email=self.email)
        elif self.user_type != 'Job Seeker' and not hasattr(self, 'user_profile'):
            UserProfile.objects.create(user=self)
    
    def __str__(self) -> str:
        return f'{self.username} | {self.email}'

class Company(models.Model):
    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='user_compnay')
    name = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    email = models.EmailField(max_length=100)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='user_profile')
    location = models.CharField(max_length=500, blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    skills = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='user/resume/', blank=True, null=True)
    cover_later = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"




