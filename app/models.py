from django.db import models

# Create your models here.
from django.contrib.admin.models import LogEntry
from django.conf import settings

from django.utils.translation import gettext_lazy as _
from django.db.models.signals import class_prepared

def override_field(sender, **kwargs):
    if sender.__name__ == "LogEntry":
        field = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            models.CASCADE,
            verbose_name=_("user"),
            db_constraint=False,
        )
        sender._meta.local_fields = [
            f for f in sender._meta.fields if f.name != "user"]
        field.contribute_to_class(sender, "user")

class_prepared.connect(override_field)
