
from .models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(pre_delete, sender=User)
def delete_profile_image(sender, instance, using, **kwargs):
    Profile.objects.get(user=instance).profile_image.delete(save=True)
