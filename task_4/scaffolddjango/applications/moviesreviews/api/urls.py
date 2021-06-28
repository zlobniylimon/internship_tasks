from rest_framework import routers

from applications.moviesreviews.api.views import MovieViewSet, ReviewViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='application.moviesreviews')
router.register(r'movies', MovieViewSet, basename='application.moviesreviews')
router.register(r'comments', CommentViewSet, basename='application.moviesreviews')
urlpatterns = router.urls
