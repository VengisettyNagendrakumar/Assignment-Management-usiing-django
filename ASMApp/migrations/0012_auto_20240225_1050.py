# Generated by Django 3.0 on 2024-02-25 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ASMApp', '0011_user_pf_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pf_image',
            field=models.ImageField(default='static/images/logo.png', null=True, upload_to='profiles/'),
        ),
    ]
