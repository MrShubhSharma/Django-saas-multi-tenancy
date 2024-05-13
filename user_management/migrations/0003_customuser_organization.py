# Generated by Django 5.0.6 on 2024-05-13 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_organization_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='user_management.organization'),
        ),
    ]
