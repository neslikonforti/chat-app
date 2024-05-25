from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import MyUserCreationForm, ProfileEditForm
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.views.generic.edit import UpdateView
from django.views import View
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
 
class ProfileView(LoginRequiredMixin,View):
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

    
class UserSignUpView(UserPassesTestMixin,CreateView):
    template_name="accounts/signup.html"
    success_url=reverse_lazy("login")
    form_class=MyUserCreationForm
    def form_valid(self, form):
       user=form.save()
       profile=Profile.objects.create(user=user)
       return redirect(self.success_url)
    def test_func(self):
        return not self.request.user.is_authenticated
    def handle_no_permission(self):
        return redirect("profile")
    

def logout_view(req):
    logout(req)
    return redirect("home")


class ProfileEditView(LoginRequiredMixin,UpdateView):
    model=Profile
    form_class=ProfileEditForm
    template_name="accounts/profile_edit.html"
    success_url=reverse_lazy("profile")
    def get_object(self):
        return self.request.user.profile