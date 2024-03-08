from django.urls import path
from . import views
from .views import Image, ImageDisplay

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('wpis/<int:pk>/', views.post_detail, name='post_detail'),
    path('image/', Image.as_view(), name='image'),
    path('image/<int:pk>/', ImageDisplay.as_view(),name='image_display'),
    path('wpis/nowy/', views.post_new, name='post_new'),
    path('wpis/<int:pk>/edycja/', views.post_edit, name='post_edit'),
]
