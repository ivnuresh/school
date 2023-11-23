from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('staff/', views.staff, name='staff'),
    path('department/<int:department_id>/', views.department_detail, name='department_detail'),
    path('get_courses/', views.get_courses, name='get_courses'),
    path('order_confirm/', views.order_confirm, name='order_confirm'),
    path('logout/', views.logout, name='logout'),
]
