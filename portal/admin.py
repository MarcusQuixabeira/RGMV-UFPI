from django.contrib import admin

from .models import Institution, Researcher,  Post, ShortPost, Project, Pub

# Register your models here.

admin.site.register(Institution)
admin.site.register(Researcher)
admin.site.register(Post)
admin.site.register(ShortPost)
admin.site.register(Project)
admin.site.register(Pub)


