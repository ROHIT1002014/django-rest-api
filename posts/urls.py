from django.urls import path
from .views import UserViewSet, PostViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', PostViewSet, basename='posts')
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls
