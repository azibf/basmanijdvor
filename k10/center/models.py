from django.db import models

# Create your models here.

class Specialization(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Specializations'

    def __str__(self):
        return self.name


class Doctor(models.Model):
    specialization = models.ForeignKey(Specialization, related_name='doctors', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    room = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='doctor_images', blank=True, null=True)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return self.name


class CEvent(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='cevent_images', blank=True, null=True)

    class Meta:
        ordering = ('date',)
        verbose_name_plural = 'CEvents'

    def __str__(self):
        return self.name


