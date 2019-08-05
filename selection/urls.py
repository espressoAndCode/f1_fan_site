from django.urls import path
from selection.views import (
    HomePageView,
    SeasonPageView,
    DriverPageView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('results/<int:year>/<int:raceId>', SeasonPageView.as_view(), name='season-page'),
    path('driver-detail/<int:year>/<int:raceId>/<int:driverId>', DriverPageView.as_view(), name='driver-page')
]
