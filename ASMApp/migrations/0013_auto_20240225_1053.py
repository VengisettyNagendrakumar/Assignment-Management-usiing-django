# Generated by Django 3.0 on 2024-02-25 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ASMApp', '0012_auto_20240225_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pf_image',
            field=models.ImageField(default='static/images/logo.png', upload_to='profiles/'),
        ),
    ]