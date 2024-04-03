from django.urls import path, include
from rest_framework.routers import DefaultRouter
from configAPP.views import *

router = DefaultRouter()
router.register(r'movies', MovieModelViewSet, basename='movies')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    # path('auth/', obtain_auth_token),
    path('move/', MovieAPIView.as_view()),
    path('actor/', ActorAPIView.as_view()),
    path('comment/', CommentApiVIev.as_view()),

    path('add_actor/', include(router.urls)),
    path('comments/', include(router.urls)),
]
