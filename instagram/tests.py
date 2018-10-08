from django.test import TestCase
from .models import Profile,Image,Comment
import datetime as dt
# Create your tests here.
class ImageTestCLass(TestCase):
    '''
    setup self instance of image
    '''
    def setUp(self):
        self.post = Image(name='Music',description='music is a southing sound that moves souls')
    
    ''' 
    test instance of image
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Image))


    '''
    test save image
    '''

    def test_save_image(self):
        self.post.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
