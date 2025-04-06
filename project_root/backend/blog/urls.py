from django.urls import path
from .views import RegisterView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('blogs/', BlogListView.as_view()),
    path('blogs/<int:pk>/', BlogDetailView.as_view()),
    path('blogs/create/', BlogCreateView.as_view()),
    path('blogs/<int:pk>/edit/', BlogUpdateView.as_view()),
    path('blogs/<int:pk>/delete/', BlogDeleteView.as_view()),
]
