from django.contrib import admin
from . models import AdminPage,Job,Team

# Register your models here.
admin.site.register(AdminPage)
admin.site.register(Job)
admin.site.register(Team)