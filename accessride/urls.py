from django.urls import path

from . import views

app_name = "accessride"

urlpatterns=[
    path('',views.home,name='home'),
    path('adminpanel',views.adminpanel,name='adminpanel'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('drivers',views.drivers,name='drivers'),
    path('logout',views.logout,name='logout'),
    path('passenger',views.passenger,name='passenger')
]