from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here.
class MyGalery_TestCases(TestCase):
    def setUp(self):
        self.new_category = Category(cat_name='Dance')
        self.new_category.save_category()
        self.new_location = Location(location_name = 'Mombasa')
        self.new_location.save_location()
        self.new_image = Image(id=1,image_name='learn', image_description='Learn 2017',image_path='media/gallery/dance-3134828_1920.jpg',image_category=self.new_category,image_location=self.new_location)
    
    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

   