from blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.template.context import RequestContext
from django.conf import settings

def setDisqus():
    try:
        return settings.DISQUSTAG
    except AttributeError:
        return None

@csrf_protect
def index(request):
    args = {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all().order_by('-posted', 'title')[:5],
    }
    return render_to_response('blog/index.html', RequestContext(request, args))

#Returns the (hopefully) singular post for that blog
def view_post(request, slug):
    args = {
    'posts': Blog.objects.filter(slug=slug).order_by('-posted', 'title')[:5],
    'slug': slug,
    }
    args['disqus'] = setDisqus()
    return render_to_response('blog/index.html', RequestContext(request, args))

#Grabs all posts with the matching foreign id of the category
def view_category(request, category):
    return render_to_response('blog/index.html', RequestContext(request,
            {
            'posts': Blog.objects.filter(category=Category.objects.filter(title=category)[0].id).order_by('-posted', 'title')[:5],
            }))
