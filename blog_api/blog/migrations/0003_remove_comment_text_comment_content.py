# Generated by Django 4.1.4 on 2023-01-18 16:46

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_profile_origin_country_remove_profile_rang_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='<h1>Write yours article here</h1>'),
        ),
    ]
