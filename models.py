from django.db import models
from django.contrib.auth.models import User, check_password

# Create your models here.
class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.nazwa
    
class MyUser(models.Model):
    SEX = [
        ("M","Mężczyzna"),
        ("F","Kobieta")
    ]
    user = models.OneToOneField(User)
    wiek = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX)
    miasto = models.CharField(max_length=150, blank=True, null=True)
    kategoria = models.ManyToManyField(Kategoria, blank=True, null=True)
    activationcode = models.IntegerField()
    
class MyBackend(object):
    def authenticate(self, username=None, password=None):
        # Check the username/password and return a User.
        try:
            user = User.objects.get(email=username)
            pwd_valid = check_password(password, user.password)
            if pwd_valid:
                return user
            else:
                return None
        except User.DoesNotExist:
            return None
    
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None    