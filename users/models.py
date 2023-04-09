import uuid
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from . import choices


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True, verbose_name=_('Email'))
    user_type = models.CharField(
        choices=choices.UserTypeChoices.choices,
        null=True,
        blank=True,
        max_length=10,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
