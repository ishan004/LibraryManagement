from django.urls import path
from accounts.views import admin_register,admin_login, logout_view

urlpatterns = [
    
    path('admin_register/', admin_register, name="admin_register"),
    path('admin_login/', admin_login, name="admin_login"),
    path('logout/', logout_view, name="logout"),
    
   
]