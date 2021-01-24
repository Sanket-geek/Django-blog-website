
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),

    #Homepage
    path('', views.index, name='index'),

    # This will load the content form App_Login
    path('account/', include('App_Login.urls')),
    
    # This will load the content form App_Blog
    path('blog/', include('App_Blog.urls')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

