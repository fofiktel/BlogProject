from django.db.models.signals import pre_delete
from .models import Post
from django.dispatch import receiver
import os
from bs4 import BeautifulSoup as bs
from blog_api.settings import BASE_DIR

@receiver(pre_delete, sender=Post)
def delete_post_images(sender, instance, using, **kwargs):
    soup = bs(instance.content, "html.parser")
    for img in soup.find_all("img"):
        os.remove(os.path.join(BASE_DIR, img.attrs.get("src")[1:]))
