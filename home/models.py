from django.db import models


# Create your models here.
class ce(models.Model):
    firstname=models.CharField(max_length=122,null=True)
    lastname=models.CharField(max_length=122,null=True)
    phone=models.CharField(max_length=12)
    subject=models.CharField(max_length=122)
    
    #def __str__(self):
    #    return self.firstname
    