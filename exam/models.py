from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.
class Exam(models.Model):
    exam = models.TextField(null=True)
    examiner_group = models.ManyToManyField(Group)

    def __str__(self):
        return self.exam


class examStatus(models.Model):
    status = models.CharField(max_length=200, null=True, default='Participated')
    user_id = models.IntegerField(null=True)
    exam_id = models.IntegerField(null=True)


class Question(models.Model):
    exams = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True)
    question = models.TextField(null=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, null=True)
    checked = models.BooleanField(null=True)

    def __str__(self):
        return self.text


class ExamResult(models.Model):
    user_id = models.IntegerField(null=True)
    exam_id = models.IntegerField(null=True)
    question_id = models.IntegerField(null=True)
    choice_id = models.IntegerField(null=True)
    choice = models.BooleanField(null=True, default=False)
