# Generated by Django 5.1.4 on 2024-12-13 21:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_remove_externallink_url_alter_externallink_spotify_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfdocument',
            name='created_by',
            field=models.ForeignKey(default='ADMIN', on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_documents', to=settings.AUTH_USER_MODEL),
        ),
    ]
