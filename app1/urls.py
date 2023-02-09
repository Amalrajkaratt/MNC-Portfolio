from django.urls import path
from . import views
app_name='app1'
urlpatterns=[
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    path('login',views.login,name='login'),
    path('loginhome/<int:id>',views.loginhome,name='loginhome'),
    path('signuphome',views.signuphome,name='signuphome'),
    path('careers',views.careers,name='careers'),
    path('careersignup',views.careersignup,name='careersignup'),
    path('clogin',views.clogin,name='clogin'),
    path('chome/<int:id>',views.chome,name='chome'),
    path('contact',views.contact,name='contact'),
    path('mail',views.mail,name='mail'),
    path('logout',views.logout,name='logout'),
    path('changepassword/<int:id>',views.changepassword,name='changepassword'),
    path('cupdate/<int:id>',views.cupdate,name='cupdate'),
]