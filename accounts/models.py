from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    bio=models.TextField(blank=True,null=True,max_length=400)
    status=models.TextField(blank=True,null=True,max_length=100)
    online=models.BooleanField(default=False)
    image=models.ImageField(blank=True,null=True,upload_to="avatars/")