# Generated by Django 3.0 on 2024-02-23 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ASMApp', '0003_auto_20240222_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='syear',
            field=models.CharField(choices=[(0, '----- Select Year -----'), (1, '1st Year'), (2, '2nd Year'), (3, '3rd Year'), (4, '4th Year')], default=0, max_length=3),
        ),
    ]
