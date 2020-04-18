from django.db import models

# Create your models here.
class Lecture(models.Model):
        l_name = models.CharField(max_length = 50)
        lecture_date = models.DateTimeField(auto_now_add= False)
        lecture_date_end = models.DateTimeField(auto_now_add= False)
        def __str__(self):
          return self.l_name
          