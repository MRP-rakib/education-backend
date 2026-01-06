
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def Home(request):
    return JsonResponse({
        'message':'system is ok',
        'status':True
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home, name='home'),
    path('api/', include('api.urls')),
    path('api/auth/', include('account.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
