
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('carlists/',include('carlists.urls')),
    path('accounts/',include('accounts.urls')),
    path('contacts/',include('contacts.urls')),
    path('servicing/',include('servicing.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
