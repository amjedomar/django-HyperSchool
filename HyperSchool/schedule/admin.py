from django.contrib import admin
from .models import Teacher, Course, Student


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration_months', 'price')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age')


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
