from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# TODO: 学习这个 receiver
@receiver(post_save, sender=User)
def create_profice(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profice(sender, instance, **kwargs):
    instance.profile.save()