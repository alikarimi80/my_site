from django.contrib import admin
from exam.models import Questions, Choices, Exams

# Register your models here.
admin.site.register(Questions)
admin.site.register(Choices)
admin.site.register(Exams)
