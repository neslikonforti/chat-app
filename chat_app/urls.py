from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("main.urls")),
]
"""1) Создать новое приложение accounts 
2) В нем сделать urls.py
3) Сделать папки templates, static 
4) Соединить его urls с главным urls.py"""