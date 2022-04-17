from django.db import models

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    #logo = CloudinaryField('image')
    #admin = models.ForeignKey(Profile,on_delete=models.CASCADE)
    health_dept = models.IntegerField(null=True, blank=True)
    police_dept = models.IntegerField(null=True, blank=True)


