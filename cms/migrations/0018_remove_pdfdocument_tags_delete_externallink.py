# Generated by Django 5.1.4 on 2024-12-14 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0017_pdfdocument_spotify_pdfdocument_youtube'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdfdocument',
            name='tags',
        ),
        migrations.DeleteModel(
            name='ExternalLink',
        ),
    ]
