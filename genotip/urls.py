from django.urls import path
from genotip import views

urlpatterns = [
    path(route='', view=views.login, name='login'),
    path(route='logout/', view=views.logout, name='logout'),
]
