from django.forms import ModelForm
from .models import *


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

class SubscribeForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'





