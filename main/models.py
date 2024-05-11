from django.db import models
from django.contrib.auth.models import User
class Chat(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    participants=models.ManyToManyField(User,related_name='chats')
class Message(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    content=models.TextField(max_length=200)
    read=models.BooleanField(default=False)
    sender=models.ForeignKey(User,related_name="messages",on_delete=models.CASCADE)
    chat=models.ForeignKey(Chat,related_name="messages",on_delete=models.CASCADE)