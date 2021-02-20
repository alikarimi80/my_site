from django.shortcuts import render
from .models import Questoins, Exams, Choices


# Create your views here.
def lists(response, id, id2):
    ls = Questoins.objects.all()
    ex = Exams.objects.get(id=id2)
    ch = Choices.objects.all()
    ty = Choices.objects.all()
    a1 = Questoins.text_set.all
    print(ty)

    # for item in ls.choices_set.all():
    #     if response.POST.get("c" + str(item.id)) == "clicked":
    #         item.checked = True
    #     else:
    #         item.checked = False
    #
    #         item.save()

    return render(response, "list.html", {"ls": ls, "ch": ch, "id": id, "choices": Choices})
