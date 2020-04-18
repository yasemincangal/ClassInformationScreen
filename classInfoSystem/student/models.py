from django.db import models

# Create your models here.

class Student(models.Model):
    department_name = models.ForeignKey("department.Department",on_delete = models.CASCADE)
    lecture_name = models.ForeignKey("lecture.Lecture",on_delete= models.CASCADE)
    studentfullname = models.CharField(max_length = 50)
    studentbdate = models.DateTimeField(auto_now_add= False)
    def __str__(self):
       return self.studentfullname
