from django.contrib import admin

# Register your models here.

from .models import *


class ModuleAdmin(admin.ModelAdmin):
    list_display = ["title", "video_link", "last_updated", "created", "course"]

    class Meta:
        model = Module


class CourseAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class Meta:
        model = Course


class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "module"]

    class Meta:
        model = Task


admin.site.register(Module, ModuleAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Task, TaskAdmin)