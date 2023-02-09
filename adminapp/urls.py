from django.urls import path
from . import views
app_name='adminapp'
urlpatterns=[
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminloginhome/1',views.adminloginhome,name='adminloginhome'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('delete1/<int:id>',views.delete1,name='delete1'),
    path('supdate/<int:id>',views.supdate,name='supdate'),
    path('acupdate/<int:id>',views.acupdate,name='acupdate'),
    path('addjob',views.addjob,name='addjob'),
    path('addteam',views.addteam,name='addteam'),
    path('jobdelete/<int:id>',views.jobdelete,name='jobdelete'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('jobedit/<int:id>',views.jobedit,name='jobedit'),
    path('addreview',views.addreview,name='addreview'),
    path('teamedit/<int:id>',views.teamedit,name='teamedit'),
    path('teamdel/<int:id>',views.teamdel,name='teamdel'),
    path('courseedit/<int:id>',views.courseedit,name='courseedit'),
    path('coursedel/<int:id>',views.coursedel,name='coursedel'),
    path('reviewedit/<int:id>',views.reviewedit,name='reviewedit'),
    path('psedit/<int:id>',views.psedit,name='psedit'),
    path('revdel/<int:id>',views.revdel,name='revdel'),
]