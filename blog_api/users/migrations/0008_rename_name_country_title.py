# Generated by Django 4.1.4 on 2023-01-18 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='name',
            new_name='title',
        ),
    ]
