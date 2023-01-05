from django.urls import path
from . import views

app_name='jboard'

urlpatterns=[
    path('',views.index)

]