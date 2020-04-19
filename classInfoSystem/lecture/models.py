from django.db import models

# Create your models here.
class Lecture(models.Model):
        l_name = models.CharField(max_length = 50,unique=True,verbose_name="Lecture Name")
        lecture_date = models.DateTimeField(auto_now_add= False,verbose_name="Lecture Start Date")
        lecture_date_end = models.DateTimeField(auto_now_add= False,verbose_name="Lecture Finish Date")
        def __str__(self):
          return self.l_name
          