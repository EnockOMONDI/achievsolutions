from django.db import models
from django.urls import reverse
from pyuploadcare.dj.models import ImageField
from imagekit.models import ImageSpecField 
from imagekit.processors import ResizeToFill 


class EventCategory(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'eventcategory'
        verbose_name_plural = 'eventcategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('achievesolapp:product_list_by_Eventcategory', args=[self.slug])

class BlogCategory(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'blogcategory'
        verbose_name_plural = 'blogcategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('achievesolapp:blog_list_by_category', args=[self.slug])


class MediaCategory(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'mediacategory'
        verbose_name_plural = 'mediacategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('achievesolapp:media_list_by_category', args=[self.slug])



class Blog(models.Model):
    blogcategory = models.ForeignKey( BlogCategory, related_name='blogs', on_delete=models.CASCADE)
    blog_name = models.CharField(max_length=100, db_index=True)
    brief_description = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    blog_story = models.TextField(blank=True)
    image = ImageField(blank=True, null=True)
   
     
    class Meta:
        ordering = ('-created_at', ) 
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.blog_name

    def get_absolute_url(self):
        return reverse('achievesolapp:blog_detail', args=[self.id, self.slug])


class Event(models.Model):
    eventcategory = models.ForeignKey(EventCategory, related_name='events', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    brief_description = models.CharField(max_length=100, db_index=True)
    date = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, db_index=True)
    brief_story = models.TextField(blank=True)
    location = models.CharField(null=True, max_length=100, db_index=True)
    venue = models.CharField(null=True, max_length=100, db_index=True)
    start_time = models.DateTimeField(null=True, blank=True)
    End_time = models.DateTimeField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = ImageField(blank=True, null=True,)
   
     
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('achievesolapp:product_list', args=[self.id, self.slug])


class Media(models.Model):
    mediacategory = models.ForeignKey(MediaCategory, related_name='medias', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ImageField(blank=True, null=True)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('achievesolapp:media_list', args=[self.id, self.slug])
