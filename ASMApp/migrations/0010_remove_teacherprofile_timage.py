# Generated by Django 3.0 on 2024-02-24 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ASMApp', '0009_teacherprofile_timage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherprofile',
            name='timage',
        ),
    ]
