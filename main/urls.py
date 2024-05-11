from django.urls import path
from .views import HomePageView, ChatPageView , CogPageView,BellPageView
urlpatterns = [
    path("",HomePageView.as_view(),name="home"),
    path("chat/",ChatPageView.as_view(),name="chat"),
    path("cog/",CogPageView.as_view(),name="cog"),
    path("bell/",BellPageView.as_view(),name="bell"),
]
