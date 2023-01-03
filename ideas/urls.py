from rest_framework import routers
from .views import VoteViewSet, IdeaViewSet
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'idea', IdeaViewSet)
router.register(r'vote', VoteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]