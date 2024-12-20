# Generated by Django 5.1.4 on 2024-12-13 23:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0015_pdfdocument_spotify_pdfdocument_youtube_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdfdocument',
            name='spotify',
        ),
        migrations.RemoveField(
            model_name='pdfdocument',
            name='youtube',
        ),
        migrations.CreateModel(
            name='ExternalLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube', models.URLField()),
                ('spotify', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pdf_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='external_links', to='cms.pdfdocument')),
            ],
        ),
    ]
