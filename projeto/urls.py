
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('contas.urls')),
    path('blog/', include('blog.urls')),
#Essa parte de cima e do blog so apaga depois mais para frente
    path('', include('home.urls')),
    path('hospedes/', include('hospedes.urls')),
    path('quartos/', include('quartos.urls')),
    path('reservas/', include('reservas.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
