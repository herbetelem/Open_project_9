from multiprocessing import AuthenticationError
import pdb
from webbrowser import get
from django.shortcuts import render, get_object_or_404
from .models import Review, Ticket
from accounts.models import UserTheme
from django.contrib.auth.models import User

# Create your views here.
def review_list(request):
    theme = get_object_or_404(UserTheme, user=request.user)
    reviews = Review.objects.all()
    context = {
        'theme': theme,
        'reviews': reviews
    }
    return render(request, 'review/post/review_list.html', context)

def ticket_list(request):
    theme = get_object_or_404(UserTheme, user=request.user)
    tickets = Ticket.objects.all()
    context = {
        'theme': theme,
        'tickets': tickets
    }
    return render(request, 'review/post/ticket_list.html', context)

def author_list(request):
    theme = get_object_or_404(UserTheme, user=request.user)
    authors = User.objects.all()
    for author in authors:
        author.nb_post_review = len(Review.objects.filter(user=author))
        all_note = Review.objects.filter(user=author)
        if len(all_note) > 0:
            author.moy_review = sum([x.rating for x in all_note]) / len(all_note)
        else:
            author.moy_review = "null"
    context = {
        'theme': theme,
        'authors': authors
    }
    return render(request, 'review/post/author_list.html', context)


def home_page(request):
    theme = get_object_or_404(UserTheme, user=request.user)
    context = {
        'theme': theme
    }
    return render(request, "review/home.html", context)


def ticket_detail(request, id: int):
    theme = get_object_or_404(UserTheme, user=request.user)
    ticket = get_object_or_404(Ticket, id=id)
    reviews = Review.objects.filter(ticket=ticket)
    context = {
        'theme': theme,
        'ticket': ticket,
        'reviews': reviews
        }
    return render(request, 'review/post/ticket_detail.html', context)


def author_detail(request, id: int):
    theme = get_object_or_404(UserTheme, user=request.user)
    author = get_object_or_404(User, id=id)
    reviews = Review.objects.filter(user=author)
    context = {
        'theme': theme,
        'author': author,
        'reviews': reviews,
        }
    return render(request, 'review/post/author_detail.html', context)