from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    url = models.TextField(max_length=100)
    pub_date = models.DateTimeField(blank=True, null=True, default=None)
    description = models.TextField(max_length=255)
    icon = models.ImageField(upload_to='icons/', blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    votes_total = models.IntegerField(blank=True, default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:50]

    def date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
