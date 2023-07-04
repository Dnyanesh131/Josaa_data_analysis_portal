from django.db import models



# Create your models here.


class Ques1(models.Model):
    SAT = models.IntegerField(null=True)
    Random = models.IntegerField(null=True)
    GPA = models.IntegerField(null=True)


class Ques2(models.Model):
    price  = models.IntegerField(null=True)
    size = models.IntegerField(null=True)

class Ques3(models.Model):
    RollNumber = models.IntegerField(null=True)
    DataFloat = models.IntegerField(null=True)
    DataInt = models.IntegerField(null=True)

class Ques4(models.Model):
    name =models.CharField(max_length = 1000)
    email = models.CharField(max_length=1000)
    bio = models.CharField(max_length=1000)
    age = models.CharField(max_length=1000)

class Datascraped(models.Model):
    
    Institute = models.CharField(max_length =100,null = True)
    Academic = models.CharField(max_length =100,null = True)
    Quota = models.CharField(max_length =100,null = True)
    SeatType = models.CharField(max_length =100,null = True)
    OpeningRank = models.IntegerField(null = True)
    ClosingRank  = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Round = models.IntegerField(null = True)
