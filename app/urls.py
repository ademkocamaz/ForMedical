from django.urls import path
from app import views

urlpatterns = [
    path(route='', view=views.index, name='index'),
    path(route='bed/<int:bed_id>/detail', view=views.bed_detail, name='bed_detail'),
    path(route='bed/<int:bed_id>/pain', view=views.PainCreateTestView.as_view(), name='pain'),
    path(route='bed/<int:bed_id>/pain/<int:pain_id>/update', view=views.UpdateWithInlinesView.as_view(), name='pain_update'),
    path(route='bed/<int:bed_id>/pain/<int:pain_id>/print', view=views.pain_print, name='pain_print')

]
