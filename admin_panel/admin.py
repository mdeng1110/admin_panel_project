from django.contrib import admin
from django.contrib.auth.models import Group, User
from api.models import Course, Instructor

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'instructor', 'enabled')

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'enabled')

# Register your models here.

# admin.site.register(Instructor)
# admin.site.register(Course)

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_header = "Admin Panel"