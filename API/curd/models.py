import statsmodels.robust.scale
from django.db import models

# Create your models here.
class Prodect_Details(models.Model):
    no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=70)
    quan=models.IntegerField()
    buyer=models.BooleanField()
