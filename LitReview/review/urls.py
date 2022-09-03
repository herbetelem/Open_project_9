from django.urls import path
from . import views

urlpatterns = [
    # Global
    path('', views.home_page, name='home_page'),
    path('profil/<id>/', views.profile_page, name='profile_page'),
    path('subscription/<id>/', views.subscription_page, name='subscription_page'),
    path('subscription_link/<id>/', views.subscribe_link, name='subscribe_link'),
    path('unsubscription_link/<id>/', views.unsubscribe_link, name='unsubscribe_link'),

    # Review
    path('reviews/', views.review_list, name='review_list'),
    path('review/add/', views.add_review, name='add_review'),
    path('review/edit/<id>/', views.edit_review, name='edit_review'),
    path('review/delete/<id>/', views.delete_review, name='delete_review'),

    # Ticket
    path('books/', views.ticket_list, name='ticket_list'),
    path('book/<id>/', views.ticket_detail, name='ticket_detail'),
    path('books/add/', views.add_ticket, name='add_ticket'),
    path('book/edit/<id>/', views.edit_ticket, name='edit_ticket'),
    path('book/delete/<id>/', views.delete_ticket, name='delete_ticket'),

    # Author
    path('author/', views.author_list, name='author_list'),
    path('author/<id>/', views.author_detail, name='author_detail'),
]
