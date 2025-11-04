from django.db import models
import uuid


class HealthCheck(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'healthcheck'
        verbose_name_plural = 'healthchecks'