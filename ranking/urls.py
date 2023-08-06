from django.urls import path
from . import views
urlpatterns = [
  path('', views.index, name='index'),
  path('rankings/', views.rankings, name='rankings'),
  path('genre/<str:genre_id>/', views.genre_ranking, name='genre_ranking'),
]