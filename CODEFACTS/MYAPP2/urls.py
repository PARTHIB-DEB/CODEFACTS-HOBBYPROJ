from django.urls import path
from  . import views

urlpatterns = [
    path('',views.index,name="HOME"),
    path('about',views.about,name="ABOUT"),
    path('python',views.python,name="PYTHON"),
    path('contact',views.contactus,name="CONTACT"),
]
