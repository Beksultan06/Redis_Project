from django.urls import path
from .views import LoginView, LogoutView, PostCreateView, PostListView, RegisterView, IndexView, ContactView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('contact/', ContactView.as_view(), name='contact'),
]