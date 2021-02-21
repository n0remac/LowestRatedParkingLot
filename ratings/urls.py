from django.urls import path
from .views import ViewRatings

urlpatterns = [
    path('', ViewRatings.as_view(), name="ViewRating"),
]