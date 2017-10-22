from django.db import models



class Mags(models.Model):
       magzine_name =models.CharField(max_length=100)
       magzine_year =models.CharField(max_length=10)
       magzine_coverpage = models.FileField()
       def __str__(self):
           return self.magzine_name + '-' + self.magzine_year  

class Cont(models.Model):
       member = models.ForeignKey(Mags , on_delete= models.CASCADE)
       page_title = models.CharField(max_length=100)
       pages= models.FileField()
       def __str__(self):
           return self.page_title