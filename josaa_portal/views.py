from django.shortcuts import render
from django.http import HttpResponse
from .models import Datareq
# Create your views here.\
from django.db.models import Avg
import json
def home(request):
    return render(request,'Josaa/home.html')

def aboutQues1(request):
    popular_branches = [
        'Computer Science and Engineering (4 Years, Bachelor of Technology)',
        'Electrical Engineering (4 Years, Bachelor of Technology)',
        'Mechanical Engineering (4 Years, Bachelor of Technology)',
    ]

    filtered_data= Datareq.objects.filter(Round = 6,SeatType='OPEN',Gender='Gender-Neutral',Academic__in = popular_branches)
    jsdata = filtered_data.values('Institute','Year','Academic','OpeningRank','ClosingRank')
    jsdata = json.dumps(list(jsdata))
    context ={
        'alldata': filtered_data,
        'jsdata' : jsdata,
    }
    return render(request,'Josaa/aboutQues1.html',context)

def aboutQues2(request):
    return render(request,'Josaa/aboutQues2.html')

def aboutQues5(request):
    return render(request,'Josaa/aboutQues5.html')


def aboutQues4(request):
    return render(request, 'Josaa/aboutQues4.html')
def aboutQues3(request):
    return render(request, 'Josaa/aboutQues3.html')