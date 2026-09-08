from django.contrib import admin
from .models import Server , MetricLog

# Register your models here.
class ServerAdmin(admin.ModelAdmin):
    list_display=['hostname','IP','environment','status']
    search_fields=['hostname','IP','environment','status']
admin.site.register(Server,ServerAdmin)

class MetricLogAdmin(admin.ModelAdmin):
    list_display=['server','cpu_usage','memory_usage','disk_usage','uptime_seconds','recorded_at']
    search_fields=['cpu_usage','memory_usage','disk_usage','uptime_seconds','recorded_at']

admin.site.register(MetricLog,MetricLogAdmin)