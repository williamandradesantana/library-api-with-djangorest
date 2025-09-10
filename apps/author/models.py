from django.db import models
from django.utils.translation import gettext_lazy as _

NATIONALITIES = [
    ("American", "American"),
    ("British", "British"),
    ("Canadian", "Canadian"),
    ("French", "French"),
    ("German", "German"),
    ("Indian", "Indian"),
    ("Japanese", "Japanese"),
    ("Russian", "Russian"),
    ("Spanish", "Spanish"),
    ("Other", "Other"),
]


# Create your models here.
class Author(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=100, blank=False)
    date_of_birth = models.DateField(verbose_name=_("Date of birth"), blank=False)
    nationality = models.CharField(
        verbose_name=_("Nationality"), choices=NATIONALITIES, blank=False, max_length=20
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))

    def __str__(self):
        return self.name
