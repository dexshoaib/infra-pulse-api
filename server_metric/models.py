from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
STATUS_CHOICES = [
    ('up', 'Up'),
    ('down', 'Down'),
    ('degraded', 'Degraded'),
    ('maintenance', 'Maintenance'),
]
ENVIRONMENT_CHOICES = [
    ('prod', 'Production'),
    ('staging', 'Staging'),
    ('dev', 'Development'),
]


class Server(models.Model):
    hostname=models.CharField(max_length=100)
    IP=models.GenericIPAddressField()
    environment=models.CharField(max_length=30,choices=ENVIRONMENT_CHOICES,default='dev')
    status=models.CharField(max_length=20, choices=STATUS_CHOICES,default='up')

    def __str__(self):
        return f"{self.hostname}-{self.IP} --{self.enviroment}-{self.status}"


class MetricLog(models.Model):
    server=models.ForeignKey(Server,on_delete=models.CASCADE,related_name='metrics')
    cpu_usage=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    memory_usage=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    disk_usage=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    uptime_seconds=models.PositiveIntegerField()
    recorded_at=models.DateTimeField()

    class Meta:
        ordering=['-recorded_at']

    def __str__(self):
        return f" {self.server.hostname}- {self.uptime_seconds} - {self.recorded_at}"