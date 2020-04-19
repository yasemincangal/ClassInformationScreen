from django.db import models

# Create your models here.

class Classroom(models.Model):
    department_name = models.ForeignKey("department.Department",on_delete = models.CASCADE,verbose_name="Department Name")
    lecture_name = models.ForeignKey("lecture.Lecture",on_delete= models.CASCADE,verbose_name="Lecture Name")
    classroom_name = models.CharField(max_length = 50,unique=True,verbose_name="Classroom Name")
    def __str__(self):
       return self.classroom_name
