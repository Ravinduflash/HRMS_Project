from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_employee, name='search_employee'),
    path('update/<int:emp_no>/', views.update_employee, name='update_employee'),
]