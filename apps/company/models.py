from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Company(BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=222)
    desc = models.CharField(verbose_name=_("Description"), max_length=222)

    def __str__(self):
        return self.name


class Vacancy(BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=222)
    desc = models.CharField(verbose_name=_("Description"), max_length=222)

    def __str__(self):
        return self.name


class Resume(BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=222)
    desc = models.CharField(verbose_name=_("Description"), max_length=222)

    def __str__(self):
        return self.name

