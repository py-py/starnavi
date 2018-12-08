from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

__all__ = ('Post', 'Like', 'STATUS', )

STATUS = (
    (-1, _('Dislike')),
    (0, _('Nothing')),
    (1, _('Like')),
)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name=_('User'))
    text = models.TextField(verbose_name=_('Text'))
    date = models.DateTimeField(verbose_name=_('Date'), auto_now_add=True)

    def count_likes(self):
        return self.likes.filter(status=1).count()

    def count_dislikes(self):
        return self.likes.filter(status=-1).count()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name=_('User'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', verbose_name=_('Post'))
    status = models.SmallIntegerField(choices=STATUS, default=0, verbose_name=_('Status'))

    class Meta:
        unique_together = ("user", "post",)
