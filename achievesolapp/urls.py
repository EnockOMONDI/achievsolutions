from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



app_name = 'achievesolapp'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^services/', views.services, name='services'),
    url(r'^programs/', views.programs, name='programs'), 
    url(r'^videos/', views.videos, name='videos'),   
    url(r'^events/', views.product_list, name='product_list'),
    url(r'^media/', views.media_list, name='media_list'),
    url(r'^blog/', views.blog_list, name='blog_list'),
    url(r'^pastevents/', views.events404, name='events404'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^appointement/', views.appointement, name='appointement'),
    url(r'^eventbooking/', views.eventbooking, name='eventbooking'),
     url(r'^(?P<blogcategory_slug>[-\w]+)/$', views.blog_list, name='blog_list_by_category'),
    url(r'^(?P<mediacategory_slug>[-\w]+)/$', views.media_list, name='media_list_by_category'),  
   
    url(r'^(?P<id>\d+)/(?P<blogcategory_slug>[-\w]+)/$', views.blog_detail, name='blog_detail'),
   
   
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
