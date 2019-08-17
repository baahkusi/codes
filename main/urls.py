from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('post/', post, name='post'),
    path('join/', join_us, name='join' ),
    path('events/', events, name='events'),
    path('resources/', resources, name='resources'),
    path('services/', services, name='services' ),
    path('contact/', resources, name='contact'),
]
