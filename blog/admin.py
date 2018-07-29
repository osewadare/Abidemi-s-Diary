
from django.contrib import admin
from .models import *

subscriber_list = []
subscribers = Subscriber.objects.all()
for item in subscribers:
    subscriber_list.append(item.email)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    list_display = ['title', 'category']

    def save_related(self, request, form, *args, **kwargs):
        super(PostAdmin, self).save_related(request, form, *args, **kwargs)
        send_mail("New Post on Abidemi's Diary", form.instance.content, 'info@plansharetech.com', subscriber_list)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    prepopulated_fields = {'slug':('title',)}


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'body']
    search_fields = ['name']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    search_fields = ['first_name']



admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentsAdmin)
admin.site.register(profile, ProfileAdmin)
admin.site.register(Setting)
