from django.urls import path
from .views import HomePageView, ChatPageView , CogPageView, BellPageView ,delete_message_view
urlpatterns = [
    path("",HomePageView.as_view(),name="home"),
    path("chat/<int:id>",ChatPageView.as_view(),name="chat"),
    path("chat/<int:id>/<int:message_id>",delete_message_view,name="message_delete"),
    path("cog/",CogPageView.as_view(),name="cog"),
    path("bell/",BellPageView.as_view(),name="bell"),
]
