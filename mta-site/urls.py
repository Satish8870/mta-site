"""
URL configuration for mta_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index, name="INDEX"),
    path('', views.mta_line, name="INDEX"),
    path('mta-line', views.mta_line, name="MTA-Line"),
    # path('about', views.about, name="MTA-About"),
    # path('service', views.service, name="MTA-Service"),
    # path('blog', views.blog, name="MTAblog"),
    # path('contact', views.contact, name="MTA-Contact"),
    # path('ajax/update/graph/', views.UpdateGraph.as_view(), name='update_graph'),
    path('ajax/update/graph/multiple', views.UpdateGraphMultiple.as_view(), name='update_graph_multiple'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
