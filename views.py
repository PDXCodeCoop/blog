from blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.template.context import RequestContext

@csrf_protect
def index(request):
    return render_to_response('blog/index.html', RequestContext(request,
            {
            'categories': Category.objects.all(),
            'posts': Blog.objects.all().order_by('-posted', 'title')[:5],
            }))

#Returns the (hopefully) singular post for that blog
def view_post(request, slug):   
    return render_to_response('blog/index.html', RequestContext(request,
            {
            'posts': Blog.objects.filter(slug=slug).order_by('-posted', 'title')[:5],
            'slug': slug,
            }))

#Grabs all posts with the matching foreign id of the category
def view_category(request, category):
    return render_to_response('blog/index.html', RequestContext(request,
            {
            'posts': Blog.objects.filter(category=Category.objects.filter(title=category)[0].id).order_by('-posted', 'title')[:5],
            }))