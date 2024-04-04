from django.contrib import admin
from .models import DepartmentModel, StudentModel

# Register your models here.

class Department(admin.ModelAdmin):
    list_display=['dep_name', 'description']
admin.site.register(DepartmentModel,Department)


class Student(admin.ModelAdmin):
    list_display = ['stu_name', 'stu_class', 'stu_email', 'stu_mobile', 'stu_department']
admin.site.register(StudentModel, Student)