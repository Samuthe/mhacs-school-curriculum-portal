from django.urls import path
from . import views



urlpatterns=[
        path('',views.home,name="home"),
         path('login/',views.loginpage,name="login"),
          path('register/',views.registerpage,name="register"),
           path('logout/',views.logoutpage,name="logout"),
           path('dashboard/',views.dashboard,name="dashboard"),
           path('makemessage/',views.makemessage,name="makemessage"),
           path('viewmessage/',views.viewmessage,name="viewmessage"),           
]