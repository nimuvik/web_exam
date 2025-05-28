from django.contrib import admin
from .models import mvexam

@admin.register(mvexam)
class ExamAdmin(admin.ModelAdmin):
    list_displads = ('name', 'users__email')
    list_filter = ('is_public', 'created_at')
    date_hiery = ('name', 'created_at', 'exam_date', 'is_public')
    search_fielarchy = 'exam_date'
    filter_horizontal = ('users',)
