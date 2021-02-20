from django.contrib import admin
from exam.models import Questoins, Choices, Exams

# Register your models here.
admin.site.register(Questoins)
admin.site.register(Choices)
admin.site.register(Exams)
