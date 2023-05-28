from django.db import models


class MOHDivision(models.Model):
    """MOH Area.  Some MOH Areas has two DS Divisons"""

    name = models.CharField(max_length=50)
    has_multiple_ds = models.BooleanField("has multiple DS divisions", blank=True)

    def __str__(self):
        return "%s" % (self.name)


class DSDivision(models.Model):
    """DS Divistion"""

    name = models.CharField("DS Division", max_length=50)
    moh_division = models.ForeignKey(
        MOHDivision, verbose_name="MOH division", on_delete=models.CASCADE
    )

    def __str__(self):
        return "%s" % (self.name)


class Institution(models.Model):
    """Hospitals, MOH offices, Units"""

    TYPES = [
        ("BHA", "BHA"),
        ("BHB", "BHB"),
        ("BHC", "BHC"),
        ("DHA", "DHA"),
        ("DHB", "DHB"),
        ("DHC", "DHC"),
        ("PMCU", "PMCU"),
        ("MOH", "MOH"),
        ("UNIT", "UNIT"),
        ("OTHER", "OTHER"),
    ]
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=5, choices=TYPES)
    ds_division = models.ForeignKey(
        DSDivision, verbose_name="DS division", on_delete=models.CASCADE
    )

    def __str__(self):
        return "%s" % (self.name)

    # Order by Name
    class Meta:
        ordering = ("name",)
