from django.db import models

# Create your models here.
class Image(models.Model):
    Image = models.ImageField(upload_to = 'images/')
    Image_name = models.CharField(max_length =30)
    Image_caption = models.TextField(max_length =40)
    Likes = models.CharField(max_length =20)
    Comments = models.TextField(max_length = 50)
    Profile = models.ForeignKey

