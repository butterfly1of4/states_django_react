from django.db import models

# Create your models here.
class States(models.Model):
    name= models.CharField(default='name', max_length=300)
    capital = models.CharField(default='capital', max_length=300)
    
        
    def __str__(self):
        return self.name