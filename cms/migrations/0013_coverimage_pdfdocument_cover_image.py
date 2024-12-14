# Generated by Django 5.1.4 on 2024-12-13 22:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_remove_pdfdocument_cover_image_delete_coverimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoverImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cover_image')),
            ],
        ),
        migrations.AddField(
            model_name='pdfdocument',
            name='cover_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cover_image', to='cms.coverimage'),
        ),
    ]
