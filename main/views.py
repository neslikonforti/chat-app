from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class HomePageView(TemplateView):
    template_name="main/home.html"
class ChatPageView(TemplateView):
    template_name="main/chat.html"
class CogPageView(TemplateView):
    template_name="main/cog.html"
class BellPageView(TemplateView):
    template_name="main/bell.html"
