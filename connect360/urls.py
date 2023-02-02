from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('permission/', include('permission.urls')),
    path('home/', include('home.urls')),
    path('areaofwork/', include('areaofwork.urls')),
    path('category/', include('category.urls')),
    path('campaigns/', include('campaign.urls')),
    path('gallery/', include('gallery.urls')),
    path('contact/', include('contact.urls')),
    path('aboutus/', include('aboutus.urls')),
    # path('reviews/', include('reviews.urls')),



]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
