import uuid
from django.db import models


# Create your models here.
def generate_filename(instance, filename):
   extension = filename.split('.')[-1]
   new_filename = "foringBlog_%s.%s" % (uuid.uuid4(), extension)
   return new_filename


class Blog(models.Model):
    
    title = models.CharField(max_length=500)
    story = models.TextField()
    blog_image = models.ImageField(upload_to=generate_filename, null=True)
    banner_image = models.ImageField(upload_to=generate_filename, null=True)
    slug = models.SlugField(max_length=255, null=True, unique=True)
# Create your models here.
