# Generated by Django 5.1.4 on 2024-12-14 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0018_remove_pdfdocument_tags_delete_externallink'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='pdfdocument',
            name='tags',
            field=models.TextField(blank=True),
        ),
    ]