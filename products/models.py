from django.db import models
# Create your models here.


# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_count = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to="images/", blank=False)
    user = models.ForeignKey('accounts.CustomUser',
                             on_delete=models.CASCADE, related_name="user")

    def like_count(self):
        return self.like.count()
