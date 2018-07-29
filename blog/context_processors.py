from .models import Post, Setting, Category, profile

def sitewidecontexts(request):
    blog_settings = Setting.objects.all()
    featured_posts = Post.objects.filter(featured='Yes')
    latest_posts = Post.objects.order_by('-pk')
    categories = Category.objects.all()
    context = {'categories': categories, 'blog_settings': blog_settings, 'latest_posts': latest_posts, 'featured_posts': featured_posts}
    return context
