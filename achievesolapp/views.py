from django.shortcuts import render, get_object_or_404
from .models import Event, Media, Blog, BlogCategory, MediaCategory, EventCategory



def product_list(request, eventcategory_slug=None):
    eventcategory = None
    eventcategories = EventCategory.objects.all()
    events = Event.objects.filter(available=True)
    if eventcategory_slug:
        eventcategory = get_object_or_404(EventCategory, slug=eventcategory_slug)
        events = Event.objects.filter(eventcategory=eventcategory)

    context = {
        'eventcategory': eventcategory,
        'eventcategories': eventcategories,
        'events': events
    }
    return render(request, 'achievesolapp/app/eventlist.html', context)

def blog_list(request, blogcategory_slug=None):
    blogcategory = None
    blogcategories = BlogCategory.objects.all()
    blogs = Blog.objects.filter(available=True)
    if blogcategory_slug:
        blogcategory = get_object_or_404(BlogCategory, slug=blogcategory_slug)
        blogs = Blog.objects.filter(blogcategory=blogcategory)

    context = {
        'blogcategory': blogcategory,
        'blogcategories': blogcategories,
        'blogs': blogs
    }
    return render(request, 'achievesolapp/app/bloglist.html', context)


def media_list(request, mediacategory_slug=None):
    mediacategory = None
    mediacategories = MediaCategory.objects.all()
    medias = Media.objects.filter(available=True)
    if mediacategory_slug:
        mediacategory = get_object_or_404(MediaCategory, slug=mediacategory_slug)
        medias = Media.objects.filter(mediacategory=mediacategory)

    context = {
        'mediacategory': mediacategory,
        'mediacategories': mediacategories,
        'medias': medias
    }
    return render(request, 'achievesolapp/app/medialist.html', context)







def blog_detail(request, id, blogcategory_slug):
    blog = get_object_or_404(Blog, id=id, slug=blogcategory_slug, available=True )
    context = {
        'blog': blog
        
    }
    return render(request, 'achievesolapp/app/blogdetail.html', context)


def home(request):
  return render(request, 'achievesolapp/app/index.html')

def about(request):
  return render(request, 'achievesolapp/app/about.html')

def programs(request):
  return render(request, 'achievesolapp/app/programs.html')

def services(request):
  return render(request, 'achievesolapp/app/services.html')

def videos(request):
  return render(request, 'achievesolapp/app/videos.html')

def contact(request):
  return render(request, 'achievesolapp/app/contact.html')

def events404(request):
  return render(request, 'achievesolapp/app/events404.html')

def appointement(request):
  return render(request, 'achievesolapp/app/bookingappointement.html')

def eventbooking(request):
  return render(request, 'achievesolapp/app/bookingevent.html')
