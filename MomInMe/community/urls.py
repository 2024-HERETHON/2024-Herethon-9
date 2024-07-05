# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('new/feed/', views.post_create, name='post_create'),  # URL for creating a new post
    path('community/', views.community, name='community'),    # URL for the community page
    path('feed/update/<int:post_id>/', views.post_update, name='post_update'),
    # Add other paths as needed for additional views
]
