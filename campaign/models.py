import datetime
from datetime import date
from django.db import models
import uuid
from category.models import *
from django.utils.translation import gettext as _
from areaofwork.models import Areaofwork

# Create your models here.
def generate_filename(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = "cmsprojects_%s.%s" % (uuid.uuid4(), extension)
    return new_filename


class Campaigns(models.Model):
    title = models.CharField(max_length=500)
    details = models.TextField()
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=255, null=True, unique=True)
    image = models.ImageField(upload_to=generate_filename, null=True)
    # start_date = models.DateTimeField(auto_now_add=True, blank=True)
    start_date = models.DateField(_("Date"), default=datetime.date.today)
    finish_date = models.DateField(_("Date"), default=date.today)

    areaofwork = models.ForeignKey(Areaofwork, on_delete=models.CASCADE, related_name='campaigns')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'campaigns')

    organized_by = models.CharField(max_length=500, null=True, blank=True)
