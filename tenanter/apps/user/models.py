from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the console.
        """
    return self.email
