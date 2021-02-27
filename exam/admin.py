from django.contrib import admin
from exam.models import *

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Exam)
# admin.site.register(Examiner)
admin.site.register(ExamResult)
# admin.site.register(QuestionResult)
