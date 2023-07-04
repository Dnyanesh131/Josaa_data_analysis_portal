from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='Josaa-home'),
    path('aboutQues4/',views.aboutQues4,name='Josaa-Ques1')
]