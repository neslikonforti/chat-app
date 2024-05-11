from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import MyUserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.views import View
from .models import Profile

class ProfileView(View):
    template_name="accounts/profile.html"
    def get(self,req):
        stx={
            "profile":Profile.objects.get(user=req.user)
        }
        return render(req,self.template_name,stx)
    

class UserLoginView(LoginView):
    template_name="accounts/login.html"
    redirect_authenticated_user=True
    success_url=reverse_lazy("home")

    
class UserSignUpView(CreateView):
    template_name="accounts/signup.html"
    success_url=reverse_lazy("login")
    form_class=MyUserCreationForm
    def form_valid(self, form):
       user=form.save()
       profile=Profile.objects.create(user=user)
       return redirect(self.success_url)
    

def logout_view(req):
    logout(req)
    return redirect("home")