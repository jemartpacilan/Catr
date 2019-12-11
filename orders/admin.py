from django.contrib import admin
from .models import Course, Tray, History
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['course_name']}),
        (None, {'fields': ['course_description']}),
        (None, {'fields': ['course_category']}),
        (None, {'fields': ['course_unit']}),
        (None, {'fields': ['course_price']}),
    ]


class TrayAdmin(admin.ModelAdmin):
    fieldssets = [
        (None, {'fields': ['created_date']}),
        (None, {'fields': ['tray_cumulative_price']}),
    ]


class HistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['history_points']}),
    ]


admin.site.register(Course, CourseAdmin)
admin.site.register(Tray, TrayAdmin)
admin.site.register(History, HistoryAdmin)
