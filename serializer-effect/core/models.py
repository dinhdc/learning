from django.db import models
import uuid


class BaseCustomModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4(), editable=False)

    class Meta:
        abstract = True
