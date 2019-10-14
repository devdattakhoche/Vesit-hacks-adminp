from django.db import models

# Create your models here
class booking(models.Model):
    
    fname=models.CharField( max_length=50)
    lname=models.CharField( max_length=50)
    email=models.EmailField(max_length=254)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pin=models.IntegerField()

def __str__(self):
        return self.fname
    
class approved(models.Model):
    
    fname=models.CharField( max_length=50)
    lname=models.CharField( max_length=50)
    email=models.EmailField(max_length=254)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pin=models.IntegerField()

def __str__(self):
        return self.fname
    

   

    