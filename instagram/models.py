from django.db import models

# Create your models here.
class Image(models.Model):
    Image = models.ImageField(upload_to = 'images/')
    Image_name = models.CharField(max_length =30)
    Image_caption = models.TextField(max_length =40)
    Likes = models.CharField(max_length =20,blank =True)
    Profile = models.ForeignKey
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    comment = models.ForeignKey

class Profile(models.Model):
    Profile_photo = models.ImageField(upload_to ='images/')
    Bio = models.TextField(max_length = 50)

class Comment(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()