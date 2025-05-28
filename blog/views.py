from django.shortcuts import render
from .models import vmexam

def exam_list(request):
    exams = vmexam.objects.filter(is_public=True)  # Только опубликованные
    return render(request, 'exams/exam_list.html', {
        'exams': exams,
        'fio': 'Вероника Мурашкина',
        'group': '241-672',
    })
