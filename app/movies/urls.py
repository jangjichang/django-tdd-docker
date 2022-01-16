from rest_framework import routers

from movies.views import MovieViewSet

router = routers.SimpleRouter()
router.register(prefix=r'api/movies', viewset=MovieViewSet, basename="movies")

urlpatterns = router.urls
