"""catr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from .routers import router
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('feedstream/', include('feedstream.urls')),
    path('registration/', include('registration.urls')),
    path('orders/', include('orders.urls')),
    path('payment/', include('payment.urls')),
    path('reviews/', include('review.urls')),
    path('chat/', include('chat.urls')),
    path('mypage/', include('mypage.urls')),
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

# api path leads to the rest_framework interface where serialized data
# can be found.

# feedstream leads to the main app (feedstream:index)
