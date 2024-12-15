from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        self.duration = (self.end_time - self.start_time).total_seconds() / 3600.0  # 持续时间以小时为单位
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title