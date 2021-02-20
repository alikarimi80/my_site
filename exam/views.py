from django.shortcuts import render
from .models import Questions, Exams, Choices


# Create your views here.
def lists(response, id1):
    ex = Exams.objects.get(id=id1)
    ls = Questions.objects.all()
    ch = Choices.objects.all()

    if response.method == "POST":
        if response.POST.get("save"):
            for item in ch:
                print(str(item.id))
                if response.POST.get("c" + str(item.id)) == "clicked":
                    print("dsffasf")
                    item.checked = True
                else:
                    item.checked = False

                item.save()

    return render(response, "list.html", {"ls": ls, "ch": ch, "id": id1, "ex": ex, "choices": Choices, "questions": Questions})
