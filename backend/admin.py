from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from backend.models import *


class BackendUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class BackendUserAdmin(UserAdmin):
    form = BackendUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('emailhunter', 'clearbit')}),
    )


class PostAdmin(admin.ModelAdmin):
    pass


class LikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, BackendUserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
