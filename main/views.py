from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class HomePageView(TemplateView):
    template_name="main/home.html"
class ChatPageView(LoginRequiredMixin,TemplateView):
    template_name="main/chat.html"
class CogPageView(LoginRequiredMixin,TemplateView):
    template_name="main/cog.html"
class BellPageView(LoginRequiredMixin,TemplateView):
    template_name="main/bell.html"
