from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from articles.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ArticleForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from taggit.models import Tag



# Create your views here.

def create(request):
    common_tags=Post.tags.most_common()[:4]
    if request.method == 'POST':
        filled_form = ArticleForm(request.POST, request.FILES)
        if filled_form.is_valid():
            savings = filled_form.save(commit=False)
            savings.save()
            filled_form.save_m2m()
            newform = ArticleForm()
            return render(request, "articles/create.html", {'articleform': newform,'common_tags':common_tags})
    else:
        form =ArticleForm()
        return render(request, "articles/create.html", {'articleform': form})

def Tagging(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Post.tags.most_common()[:4]
    allPosts = Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'allPosts':allPosts,
    }
    return render(request, 'articles/articleHome.html', context)

def articleHome(request): 
    allPosts= Post.objects.all().filter(category=3)
   
    
    paginator = Paginator(allPosts, 18)
    page = request.GET.get('page')
    try:
        allPosts = paginator.page(page)
    except PageNotAnInteger:
        allPosts = paginator.page(1)
    except EmptyPage:
        allPosts = paginator.page(paginator.num_pages)
    context={'allPosts': allPosts, 'page': page}

    return render(request, "articles/articleHome.html", context)

def roboticsHome(request): 
    allPosts= Post.objects.all().filter(category=1)
    paginator = Paginator(allPosts, 18)
    page = request.GET.get('page')
    try:
        allPosts = paginator.page(page)
    except PageNotAnInteger:
        allPosts = paginator.page(1)
    except EmptyPage:
        allPosts = paginator.page(paginator.num_pages)
    context={'allPosts': allPosts, 'page': page}

    return render(request, "articles/roboticsHome.html", context)

def codingHome(request): 
    allPosts= Post.objects.all().filter(category=2)
    paginator = Paginator(allPosts, 18)
    page = request.GET.get('page')

    try:
        allPosts = paginator.page(page)
    except PageNotAnInteger:
        allPosts = paginator.page(1)
    except EmptyPage:
        allPosts = paginator.page(paginator.num_pages)
    context={'allPosts': allPosts, 'page': page}

    return render(request, "articles/codingHome.html", context)


def articlePost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    post.save()
    
    
    context={'post':post}
    return render(request, "articles/articlePost.html", context)


def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    print('Baibhav')
    return render(request, 'articles/search.html', params)

def error(request):
    return render(request, 'articles/error.html')
