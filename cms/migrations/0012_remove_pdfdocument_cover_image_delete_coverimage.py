# Generated by Django 5.1.4 on 2024-12-13 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_coverimage_pdfdocument_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdfdocument',
            name='cover_image',
        ),
        migrations.DeleteModel(
            name='CoverImage',
        ),
    ]
