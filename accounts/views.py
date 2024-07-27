
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetCompleteView,PasswordResetConfirmView,PasswordResetDoneView
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
    
class MyPasswordChangeView(LoginRequiredMixin,PasswordChangeView):
    template_name="accounts/password_change.html"
    success_url=reverse_lazy("password_change_done")

class MyPasswordChangeDoneView(LoginRequiredMixin,PasswordChangeDoneView):
    template_name="accounts/password_change_done.html"

#1.Человек должен получить страницу, в котором заполняет почту, куда будет отправлено письмо
class MyPasswordResetView(PasswordResetView):
    template_name="accounts/password_reset.html"
    html_email_template_name="account/password_reset_email.html"
    email_template_name="account/password_reset_email.html"
#2.Человек должен получить страницу, в котором написано "На твою почту отправили письмо, проверь его!"
class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name="accounts/password_reset_done.html"
#3.Человек должен получить страницу, в котором заполняет себе новый пароль и его потверждает
class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name="accounts/password_reset_confirm.html"
#4.Человек должен получить страницу, в котором заполняет написано "Твой пароль успешно восстановлен! Теперь можно войти в аккаунт!"
class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name="accounts/password_reset_complete.html"