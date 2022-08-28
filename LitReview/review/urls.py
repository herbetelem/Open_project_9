from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.review_list, name='review_list'),
    path('books/', views.ticket_list, name='ticket_list'),
    path('author/', views.author_list, name='author_list'),
    path('', views.home_page, name='home_page'),
    path('book/<id>/', views.ticket_detail, name='ticket_detail'),
    path('author/<id>/', views.author_detail, name='author_detail'),
]
