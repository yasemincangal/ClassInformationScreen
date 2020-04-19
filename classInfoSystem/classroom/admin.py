from django.contrib import admin
from .models import Classroom

# Register your models here.
@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ["classroom_name","lecture_name"]
    list_display_links=["classroom_name","lecture_name"]
    class Meta:
        model = Classroom
