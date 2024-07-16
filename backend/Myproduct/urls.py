from django.urls import path
from .views import Home,Productlist,Vehicule,Immobilier,Informatique,Loisir
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('products/',Productlist.as_view(),name='listProduit'),
    path('vehicule/',Vehicule.as_view(),name='Vehi'),
    path('immobilier/',Immobilier.as_view(),name='Immo'),
    path('informatique/',Informatique.as_view(),name='Info'),
    path('loisir/',Loisir.as_view(),name='Lois'),


]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
