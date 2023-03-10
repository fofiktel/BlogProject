# Generated by Django 4.1.4 on 2023-01-18 10:57

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='images/profile_avatar/default_avatar.jpg', upload_to=users.models.create_path),
        ),
    ]
