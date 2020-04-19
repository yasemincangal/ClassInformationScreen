from django.contrib import admin
from .models import Lecture

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ["l_name","lecture_date","lecture_date_end"]
    list_display_links=["l_name","lecture_date","lecture_date_end"]
    class Meta:
        model = Lecture
