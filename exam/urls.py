from django.conf.urls import url
from exam import views
from django.urls import path

# SET THE NAMESPACE!
app_name = 'exam'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    path('<int:id>/<int:id2>', views.lists),
]
