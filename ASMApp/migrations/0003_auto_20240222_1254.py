# Generated by Django 3.0 on 2024-02-22 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ASMApp', '0002_studentprofile_teacherprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherprofile',
            name='tdesg',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='tsubject',
            field=models.CharField(max_length=50),
        ),
    ]
