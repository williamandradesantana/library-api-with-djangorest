from django.db import models
from django.utils.translation import gettext_lazy as _

from ..author.models import Author

GENDERS = [
    ("Fiction", "FICTION"),
    ("Fantasy", "FANTASY"),
    ("Mystery", "MYSTERY"),
    ("Romance", "ROMANCE"),
    ("Biography", "BIOGRAPHY"),
    ("Science", "SCIENCE"),
]


class Book(models.Model):
    isbn = models.CharField(
        verbose_name=_("ISBN"), max_length=20, blank=False, unique=True
    )
    title = models.CharField(verbose_name=_("Title"), max_length=150, blank=False)
    publish_date = models.DateField(verbose_name=_("Publish Date"), blank=False)
    gender = models.CharField(verbose_name=_("Gender"), choices=GENDERS, blank=False)
    price = models.DecimalField(
        verbose_name=_("Price"),
        max_digits=18,
        decimal_places=2,
        blank=False,
        null=False,
    )

    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, verbose_name=_("Author"), related_name="books"
    )

    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))

    def __str__(self):
        return f"{self.title} - {self.author.name}"
