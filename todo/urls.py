from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('deals.urls', namespace='deals')),
    path('page/', include('static_pages.urls', namespace='static_pages')),
    path('admin/', admin.site.urls),
]
3

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
