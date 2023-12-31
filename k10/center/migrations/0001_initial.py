# Generated by Django 4.2.7 on 2023-11-12 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='cevent_images')),
            ],
            options={
                'verbose_name_plural': 'CEvents',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Specializations',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('room', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='doctor_images')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='center.specialization')),
            ],
            options={
                'verbose_name_plural': 'Doctors',
                'ordering': ('name',),
            },
        ),
    ]
