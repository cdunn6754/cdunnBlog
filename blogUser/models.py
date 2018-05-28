from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="blogUser"
        )

    # I want to make the functionality to allow
    # people to make blog posts
    # but I think that I will only let most people write comments
    # so this defaults to False
    blogPoster = models.BooleanField(default=False)

    # Same thing but for people to make comments
    # the default here is to allow it
    commentPoster = models.BooleanField(default=True)

    def __str__(self):
        return ("{} {}".format(self.user.first_name,  self.user.last_name))
