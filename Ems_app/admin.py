from django.contrib import admin

from . models import EmployeeDetails,Role,Department
# Register your models here.
admin.site.register(EmployeeDetails)
admin.site.register(Role)
admin.site.register(Department)