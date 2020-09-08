from django.db import models


class TwitItem(models.Model):
    # title = models.CharField(max_length=30, default='')
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.body
