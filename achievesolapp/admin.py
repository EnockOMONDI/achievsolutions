from django.contrib import admin
from .models import EventCategory, Event, Blog, Media, BlogCategory, MediaCategory


class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(EventCategory, EventCategoryAdmin)

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(BlogCategory, BlogCategoryAdmin)

class MediaCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(MediaCategory, MediaCategoryAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'brief_description', 'location', 'price', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    # list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Event, EventAdmin,)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_name', 'slug', 'brief_description', 'blog_story', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    # list_editable = [ 'available']
    prepopulated_fields = {'slug': ('blog_name',)}


admin.site.register(Blog, BlogAdmin,)



class MediaAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    # list_editable = ['document', 'available', 'perfomance_card']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Media, MediaAdmin,)

