from django.db import models
from django.utils import timezone
from users.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Theme(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author')
    content = RichTextUploadingField(default='<h1>Write yours article here</h1>')
    theme = models.ManyToManyField(Theme, related_name='theme')


class Comment(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField(default='')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_id = models.IntegerField('self', null=True)

    def __str__(self):
        return f'Comment to {self.post} with {self.text}'
