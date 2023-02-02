from django.db import models
from users.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Theme(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    content = RichTextUploadingField(default='<h1>Write yours article here</h1>')
    theme = models.ManyToManyField(Theme, related_name='theme')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField(default='')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE, blank=True,related_name='children')
    level = models.IntegerField(default=0)

    def __str__(self):
        return f'Comment to {self.post} with {self.text}'
