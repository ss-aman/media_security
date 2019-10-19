from django.conf import settings
from django.conf.urls.static import static

from .views import MediaView


urlpatterns = static(settings.MEDIA_URL, view=MediaView.as_view())
