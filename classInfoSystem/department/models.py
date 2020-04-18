from django.db import models

# Create your models here.


class Department(models.Model):
    d_name = models.CharField(max_length = 50,verbose_name="Department")
    def __str__(self):
       return self.d_name