# Generated by Django 5.1.4 on 2024-12-14 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_remove_pdfdocument_spotify_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfdocument',
            name='spotify',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pdfdocument',
            name='youtube',
            field=models.URLField(blank=True, null=True),
        ),
    ]
