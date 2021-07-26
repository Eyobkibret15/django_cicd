from django.db import models

# Create your models here.
class student(models.Model):
    class choice(models.Choices):
        eyob = "eyoba"
        miki = "miko"

    name = models.CharField(max_length=5, choices=choice.choices)
    grade = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.name