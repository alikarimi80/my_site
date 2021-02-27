from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
@login_required
def lists(response, id1):
    ex = Exam.objects.get(id=id1)
    ls = Question.objects.all()
    ch = Choice.objects.all()
    exs = examStatus.objects

    if response.method == "POST":
        if response.POST.get("save"):
            for item in ch:
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.checked = True
                    examResultTable = ExamResult.objects.create(user_id=response.user.id, exam_id=ex.id,
                                                                question_id=item.questions.id, choice_id=item.id,
                                                                choice=item.checked)

                else:
                    item.checked = False
                    examResultTable = ExamResult.objects.create(user_id=response.user.id, exam_id=ex.id,
                                                                question_id=item.questions.id, choice_id=item.id,
                                                                choice=item.checked)

                item.save()
                examResultTable.save()
                ex.status = 'Participated'
                ex.save()
            examResultStatus = examStatus.objects.create(user_id=response.user.id, exam_id=ex.id)
            examResultStatus.save()

    return render(response, "exam/list.html",
                  {"ls": ls, "ch": ch, "id": id1, "ex": ex, "choices": Choice, "questions": Question})


@login_required
def examiner(request):
    userGroup = list(request.user.groups.all())
    y = list(Exam.objects.all())

    exam = []
    aexam=[]
    upexam = []
    aexamid = []
    pexam = []
    pexamid = []
    examGroupId = []
    examgrouplist = []
    userGroupId = []

    participated = list(examStatus.objects.filter(user_id=request.user.id).values('exam_id'))
    for i in participated:
        pexamid.append(i['exam_id'])
    pexamid = list(dict.fromkeys(pexamid))
    for i in range(len(y)):
        x = list(Exam.objects.get(id=i + 1).examiner_group.all())
        examgrouplist.append(x)
    for t in examgrouplist:
        for y in range(len(t)):
            examGroupId.append(t[y].id)

    for j in range(len(userGroup)):
        userGroupId.append(userGroup[j].id)
    examGroupId = list(dict.fromkeys(examGroupId))
    for i in userGroupId:
        for j in examGroupId:
            if i == j:
                x = Group.objects.get(id=i)
                aexam.append(list(x.exam_set.all()))
                # aexamid.append(Exam.objects.filter(examiner_group__permissions__group=j))
    for i in aexam:
        for j in range(len(i)):
            aexamid.append((i[j].id))
    aexamid = list(dict.fromkeys(aexamid))

    upexamid = list(list(set(aexamid) - set(pexamid)))

    for i in aexamid:
        exam.append(Exam.objects.get(id=i))
    for i in pexamid:
        pexam.append(Exam.objects.get(id=i))
    for i in upexamid:
        upexam.append(Exam.objects.get(id=i))

    if aexamid != 0:
        return render(request, 'exam/examiner.html',
                      {'pexam': pexam, 'upexam': upexam, 'exam': exam})
    else:
        return HttpResponse("<h1>You don't have any exam yet</h1>")
