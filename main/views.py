from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Chat, Message
from django.contrib import messages
from django.contrib.auth.models import User

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
def delete_message_view(req,id,message_id):
    if message_id:
        if Message.objects.filter(id=message_id).exists():
            message=Message.objects.get(id=message_id)
            message.delete()    
            chat=Chat.objects.get(id=id)
            if len(chat.messages.all()) == 0:
                chat.delete()
                return redirect("chat",id=0)
    return redirect("chat",id=id)
 
class FindPageView(LoginRequiredMixin,View):
    template_name="main/find.html"
    def get(self,req):
        name=req.GET.get("username")
        search=[]
        users= User.objects.filter(username__contains=name)
        print(users)
        for user in users:
            if user.username == req.user.username:
                continue
        
            search.append(
                        user
                    )
        stx={
            "search": search,
            "open_chat": None,
            "chat_to": None,
            "name": name,
        }

        return render(req,self.template_name,stx)
    def post(self,req):
        pass

class FindPageChatView(LoginRequiredMixin,View):
    template_name="main/find.html"
    def get(self,req,id,name):
        participants=User.objects.filter(id__in=[id,req.user.id])
        chats=Chat.objects.filter(participants__id=id).filter(participants__id=req.user.id)
        if len(chats) > 0:
            return redirect("chat",id=chats[0].id)
        search=[]
        users= User.objects.filter(username__contains=name)
        print(users)
        for user in users:
            if user.username == req.user.username:
                continue
        
            search.append(
                        user
                    )
        stx={
            "search": search,
            "open_chat": None,
            "chat_to": id,
            "name": name,
        }

        return render(req,self.template_name,stx)
    def post(self,req,id,name):
        chat=Chat.objects.create()
        user1=req.user
        user2=User.objects.get(id=id)
        chat.participants.add(user1,user2)
        chat.save()
        message=req.POST.get('message')
        Message.objects.create(content=message,sender=user1,chat=chat)
        return redirect("chat",id=chat.id)