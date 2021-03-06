"""onlineportfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from onlineportfolio import views as homeview
from django.conf import settings
from django.conf.urls.static import static
import notifications.urls

urlpatterns = [
    url(r'^$',homeview.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^project/', include('project.urls')),
    url(r'^public/', include('public.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications'))
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
