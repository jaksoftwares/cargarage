from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Automatically create a UserProfile for the new User if one doesn't exist yet.
    """
    if created:
        # Ensure the profile is created only once
        UserProfile.objects.get_or_create(user=instance)
