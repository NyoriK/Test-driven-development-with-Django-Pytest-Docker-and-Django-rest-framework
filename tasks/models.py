from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)

    def get_excerpt(self, total_char):
        return self.title[:total_char]
