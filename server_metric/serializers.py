from rest_framework import serializers
from .models import Server, MetricLog


class MertricLogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=MetricLog
        
        fields=['cpu_usage','memory_usage','disk_usage','uptime_seconds','recorded_at']

class ServerSerializer(serializers.ModelSerializer):
    metrics=MertricLogSerializer(read_only=True,many=True)
    class Meta:
        model=Server
        fields=['hostname','IP','environment','status','metrics']
        

