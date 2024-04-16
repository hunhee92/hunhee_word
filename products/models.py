from django.db import models

# Create your models here.


# Create your models here.
class Products(models.Model):
    content = models.CharField(max_length=255)
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    post_count = models.IntegerField(default=0)
    price = models.IntegerField()
    image = models.ImageField(upload_to="images/", blank=True)
