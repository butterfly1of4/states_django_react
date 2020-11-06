from django.urls import path
from . import views

urlpatterns = [
    path('', views.StateAPI.as_view()),
    # , name='states'
       
]