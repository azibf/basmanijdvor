from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name


class MEvent(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='mevent_images', blank=True, null=True)

    class Meta:
        ordering = ('date',)
        verbose_name_plural = 'MEvents'

    def __str__(self):
        return self.name
