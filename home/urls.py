from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='accueil'),
    path('contact/', views.ContactPage, name='contact'),
    path('galerie/', views.GalleryPage, name='galerie'),
    path('reservation/', views.ReservationSeance, name='reservation'),
    path('confirmation/', views.confirmationPage, name='confirmation')
]

