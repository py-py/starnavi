from django.contrib import admin
from backend.models import *


class PostAdmin(admin.ModelAdmin):
    pass


class LikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
