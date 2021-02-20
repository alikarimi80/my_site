from django.db import models


# Create your models here.
class Exams(models.Model):
    exam = models.TextField(null=True)

    def __str__(self):
        return self.exam


class Questoins(models.Model):
    exams = models.ForeignKey(Exams, on_delete=models.CASCADE, null=True)
    question = models.TextField(null=True)

    def __str__(self):
        return self.question


class Choices(models.Model):
    questions = models.ForeignKey(Questoins, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, null=True)
    checked = models.BooleanField(null=True)

    def __str__(self):
        return self.text
