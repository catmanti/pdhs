from django.db import models
from pu.models import DSDivision


class Population(models.Model):
    """Mid Year Population Data"""

    ds_division = models.ForeignKey(
        DSDivision,
        verbose_name="DS Division",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="ds_population",
    )
    year = models.IntegerField(blank=True, null=True)
    population = models.IntegerField(
        blank=True, null=True, verbose_name="Mid Year Population"
    )

    def __str__(self):
        return "%s %s %s" % (self.ds_division, self.year, self.population)

    class Meta:
        # To make a composite Primary key
        unique_together = (("ds_division", "year"),)
        ordering = ("-year", "-ds_division")
