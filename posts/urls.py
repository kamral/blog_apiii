from .serializers import PostSerializer
from .views import PostApiView, PostDetailApiView
from django.urls import path

urlpatterns=[
    path('<int:pk>/', PostDetailApiView.as_view()),
    path('', PostApiView.as_view())
]