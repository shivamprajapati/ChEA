from django.db import models
from django.core.urlresolvers  import reverse

class Events(models.Model):
       event_title =models.CharField(max_length=100)
       event_desc =models.CharField(max_length=1000)
       event_image =models.FileField()
       def __str__(self):
           return self.event_title



class Eve_pics(models.Model):
        event= models.ForeignKey (Events, on_delete=models.CASCADE)
        eve_pics = models.FileField()
        eve_date = models.CharField(max_length=100)
        def __str__(self):
           return self.eve_date
