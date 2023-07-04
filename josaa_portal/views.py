from django.shortcuts import render
from django.http import HttpResponse
from .models import Ques4
# Create your views here.\
def home(request):
    return render(request,'Josaa/home.html')

def aboutQues4(request):
    labels=[]
    data = []

    queryset = Ques4.objects.order_by('age')[:6]
    for person in queryset:
        labels.append(person.name)
        data.append(person.age)
    return render(request,'Josaa/aboutQues4.html',{
        'labels' : labels,
        'data' : data
    })