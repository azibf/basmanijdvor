# Generated by Django 4.2.7 on 2023-11-14 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_item_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mevent',
            options={'ordering': ('date',), 'verbose_name_plural': 'MEvents'},
        ),
    ]