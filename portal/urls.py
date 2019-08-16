from django.urls import path

from . import views

app_name = 'portal'
urlpatterns = [
    path('', views.home, name='home'),
    path('researchers/', views.researchers, name='researchers'),
    path('researcher/<int:researcher_id>/', views.researcher_detail, name='researcher_detail'),
    path('posts/', views.posts, name='posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('history/', views.history, name='history'),
    path('projects/', views.projects, name='projects'),
    path('line_con/', views.line_con, name='line_con'),
    path('line_mel/', views.line_mel, name='line_mel'),
    path('papers/', views.pubs, name='pubs'),
]