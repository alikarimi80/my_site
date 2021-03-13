from django.contrib import admin
from exam.models import *

# Register your models here.
admin.site.register(Exam)
admin.site.register(ExamResult)

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline,
    ]
admin.site.register(Question,QuestionAdmin)