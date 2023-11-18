from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.MovieListView.as_view(), name='index'),  # edite esta linha
    path('search/', views.search_movies, name='search'), # adicione esta linha
    path('create/', views.create_movie, name='create'), # adicione esta linha
    path('<int:movie_id>/', views.detail_movie, name='detail'), # adicione esta linha
    path('update/<int:movie_id>/', views.update_movie, name='update'), # adicione esta linha
    path('delete/<int:movie_id>/', views.delete_movie, name='delete'), # adicione esta linha
     path('<int:movie_id>/review/', views.create_review, name='review'), # adicione esta linha
]