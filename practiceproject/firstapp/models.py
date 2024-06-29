from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=500)
    
    def __str__(self) :
        
        return self.first_name + " "+ self.last_name
        
    

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    relase_date = models.DateField()
    
    rating = (
        (1, "worst"),
        (2,'good'),
        (3, 'better'),
        (4,'best'),
        (5,'Excellent'),
    )
    nums_strs = models.IntegerField(choices=rating)
    
    def __str__(self):
        return self.name + " Rating : "+ str(self.nums_strs)
    