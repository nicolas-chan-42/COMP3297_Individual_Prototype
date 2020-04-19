from django.db import models


# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50, help_text="Name of Patient")
    id_number = models.CharField(
        verbose_name="ID Number", max_length=10,
        help_text="Identity Document Number")
    date_of_birth = models.DateField(help_text="Date of Birth")
    date_confirmed = models.DateField(
        help_text="Date on which the case was confirmed")
    case_number = models.PositiveIntegerField(
        unique=True, help_text="Case Number")
    locations = models.ManyToManyField("Location", through="Visit")

    class Meta:
        ordering = ["-date_confirmed"]

    def __str__(self):
        return f"[{self.case_number}] {self.name}"


class Location(models.Model):
    name = models.CharField(max_length=100,
                            help_text="Name of Location Visited")
    address = models.CharField(
        blank=True, max_length=250,
        help_text="Address (if listed in Geodata datasets)")
    district = models.CharField(max_length=50, help_text="District")
    x_coord = models.IntegerField(help_text="X-Grid Coordinates")
    y_coord = models.IntegerField(help_text="Y-Grid Coordinates")

    def __str__(self):
        if self.address:
            return f"{self.name} ({self.address}, {self.district})"
        else:
            return f"{self.name} (---, {self.district})"


class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    details = models.CharField(blank=True, max_length=100)
    category = models.CharField(
        max_length=50,
        help_text="Category of the location with respect to patient movements")

    def __str__(self):
        return f"{self.patient} <-> {self.location}"
