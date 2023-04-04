from django.urls import path, include

urlpatterns = [
    path('', include('houses.urls.v1')),

]