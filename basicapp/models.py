from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import CustomUserManager

branch_choices=(("CE","CE"),("CSE","CSE"),("ME","ME"),("ECE","ECE"),("EI","EI"),("EE","EE"))
reason_choices=(("Medical","Medical"),("Inter-NIT","Inter-NIT"),("Others","Others"))
class Application(models.Model):
    name=models.CharField(max_length=30)
    branch=models.CharField(max_length=6,choices=branch_choices,default="CE")
    schId=models.PositiveSmallIntegerField()
    reason=models.CharField(max_length=20,choices=reason_choices,default="Medical")
    explain=models.TextField(null=True)
    start_date=models.CharField(max_length=20)
    end_date=models.CharField(max_length=20)
    created_on=models.DateTimeField(default=timezone.now)
    approved=models.BooleanField(default=False)
    
    document=models.FileField(upload_to='documents/')
    
    def approve(self):
        self.approved=True
        self.save()
        
    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return str(self.schId)
    
class Register(AbstractBaseUser, PermissionsMixin):
    schId=models.IntegerField(default="",unique=True)
    name=models.CharField(max_length=30)
    is_hod=models.BooleanField(default=False)
    branch=models.CharField(max_length=6,choices=branch_choices,default="CE")
    email=models.EmailField()
    password1=models.CharField(max_length=30)
    password2=models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'schId'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    def get_absolute_url(self):
        return reverse('apply')
 
    def __str__(self):
        return str(self.schId)
    
"""class HODRegister(models.Model):
    tid=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    branch=models.CharField(max_length=6,choices=branch_choices,default="CE")
    
    email=models.EmailField()
    password1=models.CharField(max_length=30)
    password2=models.CharField(max_length=30)
    
    def __str__(self):
        return str(self.tid)"""