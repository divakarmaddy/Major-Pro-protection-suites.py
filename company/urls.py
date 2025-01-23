from django.urls import path
from. import views

urlpatterns=[
    path('', views.registerpage),
    path('userlog/', views.userlog),
    path('adminlog/', views.adminlog),
    path('adminhome/', views.adminhome),
    path('pending/', views.pending),
    path('approve/<int:id>/', views.approve),
    path('approved/', views.approved),
    path('operations/', views.operations),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('upload/', views.upload),
    path('viewimage/', views.imgview),
    path('demo/', views.demo),
    path('temp1/', views.temp1),



]