# Generated by Django 5.1.4 on 2024-12-13 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_coverimage_pdfdocument_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfdocument',
            name='cover_image',
            field=models.ImageField(default='jj', upload_to='cover_image'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CoverImage',
        ),
    ]