from django.urls import path
from selection import views

urlpatterns = [
    path('', views.home),
    path('results/<int:year>/<int:raceId>', views.results)
]
