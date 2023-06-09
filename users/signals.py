from django.db.models.signals import post_save, post_delete # for django signals.
from django.dispatch import receiver # decorators for signals.
from django.contrib.auth.models import User
from users.models import Profile


# For reference.
# @receiver(post_save, sender=Profile) # this is similar to post_save.connect()
# def updatedProfile(sender, instance, created, **kwargs):
#    print("Profile updated.")
#    print("Instance: ", instance)   # prints instance of the profile.
#    print("Sender: ", sender) # prints object of sender i.e users.models.Profile
#    print("Created: ", created) # prints True if new profile is created else print False

# @receiver(post_delete, sender=Profile) # this is similar to post_save.connect()
# def deleteProfile(sender, instance, **kwargs):
#     print("Deleting...")
#     print("Instance", instance) # prints user i.e instance in console.

# post_save.connect(updatedProfile, sender=Profile) # trigger updateProfile when sender -> Profile model is called. 

# post_delete.connect(deleteProfile, sender=Profile) # trigger deleteProfile when Profile model is deleted.


# When user is created what signals to send or perform
def createdProfile(sender, instance, created, **kwargs):   # what to do when user is created.
    if created:
        user = instance # select user as instance when opening profile table in db.
        profile = Profile.objects.create( # when user is created also create a profile prefilled with username and email
            user = user,                # fill profile table with user when new user is created.
            username = user.username,   # fill profile table with user's username when new user is created.
            email = user.email,         # fill profile table with user's email when new user is created.
        )

post_save.connect(createdProfile, sender=User)  # When the user is created connect the post_save signal with createdProfile function.


# When user is deleted from user table, it will remove profile from the table because of models.CASCADE in Profile model.
# we have a problem now when the admin deleted profile only user will not be deleted.

# delete user when profile is deleted.
def deleteUser(sender, instance, **kwargs):     # on deleting profile delete user too.
    user = instance.user        # take the instance of Profile user.
    user.delete()               # delete user

post_delete.connect(deleteUser, sender=Profile) # when the Profile is deleted connect the post_delete with deleteUser function.
