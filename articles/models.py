from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from taggit.managers import TaggableManager


# Create your models here.


class Post(models.Model):
    choices=((1,"Arduino & Robotics"),(2,"Programming"),(3,"Articles"))
    sno = models.AutoField(primary_key = True)
    title = models.CharField( max_length=255)
    image = models.ImageField(upload_to='images/') 
    category =models.IntegerField(choices=choices)
    slug = AutoSlugField(populate_from='title')
    content = HTMLField()
    author = models.CharField( max_length=50)
    tags = TaggableManager()
    

    def __str__(self):
        return self.title + 'by' +  self.author

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'pk': self.pk})

    


