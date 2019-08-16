from django.contrib import admin

from .models import Institution, Researcher, Paper, Post, ShortPost, Project

# Register your models here.

admin.site.register(Institution)
admin.site.register(Researcher)
admin.site.register(Paper)
admin.site.register(Post)
admin.site.register(ShortPost)
admin.site.register(Project)

