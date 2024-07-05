from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    baby_id = models.CharField(max_length=100)
    baby_birthdate = models.DateField()
    gender_choices = [
        ('M', '남성'),
        ('F', '여성'),
        ('O', '기타'),
    ]
    baby_gender = models.CharField(max_length=1, choices=gender_choices)
    mom_id = models.CharField(max_length=100)
    mom_birthdate = models.DateField()

    def __str__(self):
        return self.user.username

class MeKeyword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keywords = models.JSONField()

class BabyKeyword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keywords = models.JSONField()
