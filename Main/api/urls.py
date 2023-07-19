from django.urls import include, path
from .views import ClassroomAPIView

urlpatterns=[
    path('rest-auth/', include('rest_auth.urls')),
    path('classroom/', ClassroomAPIView.as_view()),
]