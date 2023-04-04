import uuid

from django.db import models


class House(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    number = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    address = models.CharField(max_length=255,blank=True, unique=True, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.address = f"{self.street} {self.number}"
        super().save(*args, **kwargs)



