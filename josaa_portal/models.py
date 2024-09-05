from django.db import models



# Create your models here.




class Datareq(models.Model):
    
    Institute = models.CharField(max_length =100,null = True)
    Academic = models.CharField(max_length = 500,null = True)

    Quota = models.CharField(max_length =100,null = True)
    SeatType = models.CharField(max_length =100,null = True)
    Gender = models.CharField(max_length=100,null=True)
    OpeningRank = models.IntegerField(null = True)
    ClosingRank  = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Round = models.IntegerField(null = True)
