from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Chat, Message
from django.contrib import messages

# Create your views here.
class HomePageView(TemplateView):
    template_name="main/home.html"

class ChatPageView(LoginRequiredMixin,View):
    template_name="main/chat.html"
    def get(self,req,id):
        chats=req.user.chats.all()
        active_chats=[]
        print(id)
        for chat in chats:
            users=chat.participants.all()
            for user in users:
                if user != req.user:
                    messages=chat.messages.all()
                    if len(messages)>0:
                        message=messages[len(messages)-1]
                    else:
                        message=None
                    active_chats.append({
                        "user": user,
                        "message": message,
                        "id": chat.id,
                    })
        if id == 0:
            chat=None
            messages=None
            chat_to=None
        else:
            chat=Chat.objects.get(id=id)
            messages=Message.objects.filter(chat=chat)
            users=chat.participants.all()
            chat_to=None
            for user in users:
                if user != req.user:
                    chat_to=user
        stx={
            "chats": active_chats,
            "chat_messages": messages,
            "open_chat": chat,
            "chat_to": chat_to
        }
        return render(req,self.template_name,stx)
    def post(self,req,id):
        content=req.POST.get("message")
        if len(content.strip()) == 0:
            messages.error(req,"Empty message")
            return redirect(f"/chat/{id}")
        chat=Chat.objects.get(id=id)
        message=Message.objects.create(chat=chat,content=content,sender=req.user)
        message.save()
        return redirect(f"/chat/{id}")
class CogPageView(LoginRequiredMixin,TemplateView):
    template_name="main/cog.html"

class BellPageView(LoginRequiredMixin,TemplateView):
    template_name="main/bell.html"
