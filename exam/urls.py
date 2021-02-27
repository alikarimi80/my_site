from django.conf.urls import url
from exam import views
from django.urls import path

# SET THE NAMESPACE!
app_name = 'exam'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    path('<int:id1>', views.lists, name="exam page"),
    path('examiner/', views.examiner, name="examiner page"),
]
