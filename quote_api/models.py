from django.db import models


class Quote(models.Model):
    """Create Quote model database"""

    quote_author = models.CharField(max_length=100)
    quote_body = models.TextField()
    context = models.CharField(max_length=255, blank=True)
    source = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.quote_author
