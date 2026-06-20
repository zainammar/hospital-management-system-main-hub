from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('add/', views.add_patient, name='add_patient'),

    path('edit/<int:id>/', views.edit_patient, name='edit_patient'),
    path('delete/<int:id>/', views.delete_patient, name='delete_patient'),
]