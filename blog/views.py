from django.shortcuts import render
from .models import Post, Category, Setting, Like, profile
from django.views.generic import TemplateView
from .forms import CommentForm, SubscribeForm
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect

def bloghome(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        subsriber_form = SubscribeForm(data=request.POST)
        if subsriber_form.is_valid():
            subsriber_form.save()
            return HttpResponseRedirect(reverse_lazy('blog:emailsubscriptionsuccess'))
    elif request.method == 'GET':
        subsriber_form = SubscribeForm()
    context = {'posts': posts, 'subsriber_form': subsriber_form}
    return render(request, 'blog/posts2/index.html', context)

class aboutmeview(TemplateView):
    template_name = 'blog/pages/aboutme.html'

def singlepostview(request, slug):
    singlepost = Post.objects.get(slug=slug)
    singlepost.views += 1
    singlepost.save()
    comments = singlepost.comments.all()

    post_comments = len(comments)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            #Create new comment object but dont save
            new_comment = comment_form.save(commit=False)

            #assign comment to singlepost
            new_comment.post = singlepost

            new_comment.save()

    else:
        comment_form = CommentForm()

    context = {'post_comments': post_comments, 'singlepost': singlepost, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'blog/posts2/single.html', context)


def singlecategoryview(request, slug):
    category = Category.objects.get(slug=slug)
    category_posts = category.posts.all()
    context = {'category': category, 'category_posts': category_posts}
    return  render(request, 'blog/posts/singlecategory.html', context)


from django.views.generic import UpdateView

class UpdateSettings(UpdateView):
    model = Setting
    template_name = 'blog/settings.html'
    fields = '__all__'
    success_url = reverse_lazy('blog:index')


def likepostview(request, slug):
    if request.method == "POST":
        new_like = Like(user=request.user, post=Post.objects.get(slug=slug))
        new_like.save()
        HttpResponseRedirect (reverse_lazy('blog:index'))


def authorview(request, publisher):
    user_posts = Post.objects.filter(publisher__username=publisher)
    context = {'user_posts' : user_posts, 'publisher': publisher}
    return render(request, 'blog/posts/author.html', context)


class emailsubscriptionsuceessview(TemplateView):
    template_name = 'blog/posts2/email_subscription_success.html'

