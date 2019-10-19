from django.views.generic import View
from django.conf import settings
from django.views.static import serve
from django.http import HttpResponseForbidden

from .models import MediaUserModel


class MediaView(View):

    def get(self, request, *args, **kwargs):
        try:
            media = MediaUserModel.objects.get(user=request.user, media_path=kwargs['path'])
        except TypeError:
            return HttpResponseForbidden()
        return serve(request, *args, document_root=settings.MEDIA_ROOT, path=media.media_path)
