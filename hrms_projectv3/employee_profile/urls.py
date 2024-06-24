from django.urls import path
from . import views

urlpatterns = [
    path('employee_profile/', views.employee_profile_view, name='employee_profile_view'),
]