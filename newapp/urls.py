from django.urls import path

from . import views
urlpatterns = [
    path('url',views.samplefn),
    path('url1',views.heading1),
    path('url2',views.h1)

    
    
]