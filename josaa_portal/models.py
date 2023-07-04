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
