from django.shortcuts import render, get_object_or_404

from .models import ShortPost, Researcher, Post, Project, Pub


def home(request):
    context = {}
    short_posts = ShortPost.objects.filter(is_cover=True)
    researchers = Researcher.objects.filter(is_cover=True)
    posts = Post.objects.filter(is_cover=True)
    context['short_posts'] = short_posts
    context['researchers'] = researchers
    context['posts'] = posts
    return render(request, 'portal/home/_home.html', context)

def researchers(request):
  researchers = Researcher.objects.order_by("first_name").all()
  context = {'researchers':researchers
  }
  return render(request, 'portal/researcher/_index.html', context)

def researcher_detail(request, researcher_id):
  context = {}
  researcher = get_object_or_404(Researcher, pk=researcher_id)
  context['researcher'] = researcher
  return render(request, 'portal/researcher/_detail.html', context)

def posts(request):
  posts = Post.objects.order_by("published_at").all()
  context = {'posts': posts
  }
  return render(request, 'portal/post/_index.html', context)

def post_detail(request, post_id):
  context = {}
  post = get_object_or_404(Post, pk=post_id)
  context['post'] = post
  return render(request, 'portal/post/_detail.html', context)

def history(request):
  context = {}
  return render(request,'portal/history/_index.html', context)

def projects(request):
  projects =  Project.objects.order_by("researcher").all()
  context = {'projects': projects
  }
  return render(request, 'portal/project/_index.html', context)

def line_con(request):
  context = {}
  project_con = Project.objects.filter(conservation=True)
  context['project_con'] = project_con
  return render(request, 'portal/line/_index_con.html', context)

def line_mel(request):
  context = {}
  project_mel = Project.objects.filter(breeding=True)
  context['project_mel'] = project_mel
  return render(request, 'portal/line/_index_mel.html', context)

def pubs(request):
  pubs = Pub.objects.order_by("-year").all()
  context = {'pubs': pubs
  }
  return render(request, 'portal/pub/_index.html', context)
