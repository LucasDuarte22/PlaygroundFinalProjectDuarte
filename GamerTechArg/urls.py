from django.urls import path
from GamerTechArg import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    #LOGIN Y LOGOUT
    path('logout/', LogoutView.as_view(template_name = 'GamerTechArg/logout.html'), name="Logout"),
    
    #COMPONENTES LISTA
    path('placasdevideo/lista', views.PlacasDeVideoListView.as_view(), name = "ListaPlacas"),
    path('motherboards/lista', views.MotherboardsListView.as_view(), name = "ListaMotherboards"),#MOTHER
    path('almacenamiento/lista', views.PlacasDeVideoListView.as_view(), name = "ListaPlacas"),#ALMACENAMIENTO
    path('memoriasram/lista', views.PlacasDeVideoListView.as_view(), name = "ListaPlacas"),#MEMOTIARAM
    path('procesadores/lista', views.PlacasDeVideoListView.as_view(), name = "ListaPlacas"),#PROCESADORES
    
    #COMPONENTES CREAR
    path('placasdevideo/nuevo', views.PlacasDeVideoCreateView.as_view(), name = "NuevaPlaca"),
    path('motherboards/nuevo', views.MotherboardsCreateView.as_view(), name = "NuevaMother"),
    
    
    
    #COMPONENTES DETALLES
    path('placasdevideo/<pk>', views.PlacasDeVideoDetailView.as_view(), name = "DetallePlaca"),
    path('motherboards/<pk>', views.MotherboardsDetailView.as_view(), name = "DetalleMother"),
    
    
    
    #COMPONENTES EDITAR
    path('placasdevideo/<pk>/editar', views.PlacasDeVideoUpdateView.as_view(), name = "EditarPlaca"),
    path('motherboards/<pk>/editar', views.MotherboardsUpdateView.as_view(), name = "EditarMother"),
    
    
    #COMPONENTES BORRAR
    path('placasdevideo/<pk>/borrar', views.PlacasDeVideoDeleteView.as_view(), name = "BorrarPlaca"),
    path('motherboards/<pk>/borrar', views.MotherboardsDeleteView.as_view(), name = "BorrarMother"),
    
]
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)