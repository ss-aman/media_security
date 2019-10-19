from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class MediaUserModel(models.Model):
    media_path = models.CharField(max_length=300)
    content_type = models.ForeignKey('contenttypes.ContentType', on_delete=models.CASCADE)
    instance = models.PositiveIntegerField()
    field = models.CharField(max_length=20)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
        verbose_name = _('Media Security Data')
        verbose_name_plural = _('Media Security Data')

    def __str__(self):
        return "Instance of - {}, Instance - {}, Created by {}".format(
            self.content_type,
            self.content_type.get_object_for_this_type(id=self.instance),
            self.user)

