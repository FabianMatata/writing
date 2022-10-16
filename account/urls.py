from django.urls import path
from . import views
from .views import create_assignment

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),

    path('', create_assignment, name='create_assignment'),
    

]