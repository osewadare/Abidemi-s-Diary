from django.db import models
from tinymce_4.fields import TinyMCEModelField
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail



class profile(User):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete='null', parent_link=True)
    profilepicture = models.FileField(upload_to='profilepictures')


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=200)
    content = TinyMCEModelField()
    featured_image = models.FileField(upload_to='featured_images', blank=True)
    publish_date = models.DateTimeField()
    category = models.ForeignKey('Category', related_name='posts', on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey(profile, default='1', related_name="posts", on_delete=models.SET_NULL, null=True)
    featured = models.CharField(choices=(('Yes', 'yes'),('No', 'No')), max_length=3, default='No')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '{} by {}'.format(self.body, self.name)


class Setting(models.Model):
    title = models.CharField("Site Title", max_length=20)
    tagline = models.CharField("Tagline", max_length=25)
    site_url = models.CharField("Site URL", max_length=50, default="http://www.site.com")
    description = models.CharField("Description", max_length=250)
    email = models.CharField("Admin Email", max_length=25)
    facebook_id = models.CharField(max_length=50)
    twitter_id = models.CharField(max_length=50)
    instagram_id = models.CharField(max_length=50)
    linkedin_id= models.CharField(max_length=50)

    def __str__(self):
        return "Settings"


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)


class Subscriber(models.Model):
    email = models.EmailField(max_length=25)

