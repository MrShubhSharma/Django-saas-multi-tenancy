# Generated by Django 5.0.6 on 2024-05-13 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0003_customuser_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='url',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]