# Generated by Django 4.1.5 on 2023-01-31 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment'),
        ),
    ]