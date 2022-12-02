from django.db import models
import uuid
from django.utils import timezone


class BaseKeyModel(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class BaseModel(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        if not self.updated_at:
            self.updated_at = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)
