from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Place (models.Model):
    title = models.CharField(max_length=200)
    text  = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="places"
    )
    image = models.ImageField(upload_to='places/', blank=True, null=True)

    def __str__(self):
        return self.text