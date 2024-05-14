from django.contrib import admin
from django.urls import path, include
from .views import LandingPageAPIView, ArtistApiView, SongSetAPIView, AlbomAPIViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
router.register("alboms", viewset=AlbomAPIViewSet)
router.register("songs", viewset=SongSetAPIView)

urlpatterns = [
    path('landing/', LandingPageAPIView.as_view(), name="landing"),
    path("", include(router.urls)),
    path('artists/', ArtistApiView.as_view(), name="artists"),
    path('admin/', admin.site.urls),
    path('api/v1/', include("music.urls")),
]