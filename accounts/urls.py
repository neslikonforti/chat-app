from django.urls import path
from .views import UserLoginView,UserSignUpView,ProfileView,logout_view,ProfileEditView
urlpatterns = [
    path("login/",UserLoginView.as_view(),name="login"),
    path("signup/",UserSignUpView.as_view(),name="signup"),
    path("profile/",ProfileView.as_view(),name="profile"),
    path("logout/",logout_view,name="logout"),
    path("profile/edit",ProfileEditView.as_view(),name='profile_edit')
]