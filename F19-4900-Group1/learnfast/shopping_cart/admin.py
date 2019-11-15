from django.contrib import admin
from .models import Schedule

admin.site.unregister(Schedule)
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['schedule_course_name', 'slug', 'price',
                    'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('schedule_course_name',)}