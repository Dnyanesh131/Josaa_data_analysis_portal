from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='Josaa-home'),
    path('aboutQues1/',views.aboutQues1,name='Josaa-Ques1'),
    path('aboutQues2/',views.aboutQues2,name = 'Josaa-Ques2'),
    path('aboutQues4/',views.aboutQues4,name = 'Josaa-Ques4'),
    path('aboutQues5/',views.aboutQues5,name = 'Josaa-Ques5'),
    path('aboutQues3/',views.aboutQues3,name = 'Josaa-Ques3'),


]