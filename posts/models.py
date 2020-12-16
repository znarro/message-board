from django.db import models


class Post(models.Model):
    text = models.TextField()

    # For a more descriptive representation of our db entry
    # by default its name is Post Object(1)
    def __str__(self):
        return self.text[:50]