from django.db import models

# Create your models here.
class Blog(models.Model):
   title=models.CharField(max_length=250)
   text=models.TextField()
   date=models.DateField()


   #intended inside the class
   def __str__ (self) :
      return self.title
   
   



