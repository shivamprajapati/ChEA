from django.db import models
from django.core.urlresolvers  import reverse

class People(models.Model):
       member_name =models.CharField(max_length=100)
       member_post =models.CharField(max_length=50)
       member_image =models.FileField()
       def __str__(self):
           return self.member_post + '-' + self.member_name       
class Bio(models.Model):
       member = models.ForeignKey (People, on_delete=models.CASCADE)
       desc= models.CharField(max_length=500)
       g_link = models.CharField(max_length=50)
       ln_link = models.CharField(max_length=50)
