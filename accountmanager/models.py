from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileData(models.Model):
    profile_picture = models.ImageField(upload_to='media/', null=True, blank=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    study_level = models.IntegerField()
    email = models.EmailField(null=True)
    bio = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.user_name
        
