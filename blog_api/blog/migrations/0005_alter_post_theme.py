# Generated by Django 4.1.4 on 2023-01-20 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_comment_content_remove_post_text_comment_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='theme',
            field=models.ManyToManyField(related_name='theme', to='blog.theme'),
        ),
    ]
