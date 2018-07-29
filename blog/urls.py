from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.bloghome, name='index'),
    url(r'posts/(?P<slug>.*)/$', views.singlepostview, name='singlepostview'),
    url(r'categories/(?P<slug>.*)/$', views.singlecategoryview, name='singlecategoryview'),
    url(r'^authors/(?P<publisher>.*)/$', views.authorview, name="authorview"),
    url(r'^aboutme$', views.aboutmeview.as_view(), name='aboutme'),
    url(r'^settings/(?P<pk>[0-9]+)/$', views.UpdateSettings.as_view(), name="settings"),
    url(r'^subscription-success/$', views.emailsubscriptionsuceessview.as_view(), name='emailsubscriptionsuccess')
]
