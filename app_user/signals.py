from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import AppUser
from django.core.exceptions import ObjectDoesNotExist
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        AppUser.objects.create(user=instance)
        print('Profile created!')
#post_save.connect(create_profile, sender=User)
@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):

    try:
        instance.profile.save()
        print('Profile updated')
    except ObjectDoesNotExist:
        AppUser.objects.create(user=instance)
        

#post_save.connect(update_profile, sender=User)