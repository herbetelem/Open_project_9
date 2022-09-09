from multiprocessing import AuthenticationError
import pdb
from webbrowser import get
from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Ticket
from accounts.models import UserFollows
from .forms import ReviewsForm, TicketsForm
from accounts.forms import UserThemeForm
from accounts.models import UserTheme
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from itertools import chain



# Create your views here.
# View global
def home_page(request):
    context = {}
    if request.user.is_authenticated:
        followings = UserFollows.objects.filter(user=request.user)
        posts = Ticket.objects.filter(user=request.user)
        for follow in followings:    
            posts = sorted(
                chain(posts, Ticket.objects.filter(user=follow.followed_user)), 
                key=lambda post: post.time_created, 
                reverse=True
            )
        reviews = Review.objects.filter(user=request.user)
        for follow in followings:    
            reviews = sorted(
                chain(reviews, Review.objects.filter(user=follow.followed_user)), 
                key=lambda post: post.time_created, 
                reverse=True
            )
        posts = sorted(
                chain(reviews, posts), 
                key=lambda post: post.time_created, 
                reverse=True
            )
        context['flux'] = posts
        context['theme'] = get_object_or_404(UserTheme, user=request.user)
        return render(request, 'global/flux.html', context)
    return render(request, 'global/home.html', context)

def my_post(request):
    context = {}
    if request.user.is_authenticated:
        posts = Ticket.objects.filter(user=request.user)
        reviews = Review.objects.filter(user=request.user)
        posts = sorted(
                chain(reviews, posts), 
                key=lambda post: post.time_created, 
                reverse=True
            )
        context['flux'] = posts
        context['theme'] = get_object_or_404(UserTheme, user=request.user)
        return render(request, 'global/flux.html', context)
    return render(request, 'global/home.html', context)

@login_required(login_url='/login/')
def profile_page(request, id: int):
    instance = get_object_or_404(UserTheme, user=request.user)
    if request.method == "POST":
        form = UserThemeForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile_page', request.user.id)
    form = UserThemeForm(instance=instance)
    user = get_object_or_404(User, id=id)
    context = {
        'user': user,
        'form': form,
    }
    if request.user.is_authenticated:
        context['theme'] = get_object_or_404(UserTheme, user=request.user)
    return render(request, 'global/profile_page.html', context)

@login_required(login_url='/login/')
def subscription_page(request, id: int):
    if request.user.id != int(id):
        return redirect("home_page")
    followings = UserFollows.objects.filter(user=request.user)
    followers = UserFollows.objects.filter(followed_user=request.user)
    context = {
        'followers': followers,
        'followings': followings
    }
    if request.user.is_authenticated:
        context['theme'] = get_object_or_404(UserTheme, user=request.user)
    return render(request, 'global/subscription_page.html', context)

@login_required(login_url='/login/')
def subscribe_link(request, id: int):
    target = get_object_or_404(User, id=id)
    UserFollows.objects.create(user=request.user, followed_user=target)
    return redirect("subscription_page", request.user.id)

@login_required(login_url='/login/')
def unsubscribe_link(request, id: int):
    target = get_object_or_404(User, id=id)
    target_follow = UserFollows.objects.filter(user=request.user, followed_user=target)
    target_follow.delete()
    return redirect("subscription_page", request.user.id)


# View about Review
@login_required(login_url='/login/')
def review_list(request):
    reviews = Review.objects.all()
    for review in reviews:
        star = ""
        for i in range(review.rating):
            star += "★"
        while len(star) < 5:
            star += "☆"
        review.rating_star = star
    context = {
        'reviews': reviews
    }
    if request.user.is_authenticated:
        context['theme'] = get_object_or_404(UserTheme, user=request.user)

    return render(request, 'review/review_list.html', context)

@login_required(login_url='/login/')
def add_review(request):
    if request.method == "POST":
        ticket = Ticket.objects.create(
            title=request.POST.get('title'), 
            author=request.POST.get('author'), 
            description=request.POST.get('description'), 
            image=request.FILES.get('image'), 
            user=request.user,
            review_done=True)
        Review.objects.create(
            rating=request.POST['review_set-0-rating'], 
            body=request.POST['review_set-0-body'], 
            headline=request.POST['review_set-0-headline'], 
            user=request.user, 
            ticket=ticket)
        context = {'theme' : get_object_or_404(UserTheme, user=request.user)}
        return redirect('home_page')


    FormReview = inlineformset_factory(parent_model=Ticket, model=Review, fields=('headline', 'rating', 'body'), form=ReviewsForm, can_delete=False)
    form_review = FormReview()
    context = {
        'form_ticket': TicketsForm(),
        'form_review': form_review,
    }
    context['theme'] = get_object_or_404(UserTheme, user=request.user)
    return render(request, 'review/add_review.html', context)

@login_required(login_url='/login/')
def request_review(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    if request.method == "POST":
        form = ReviewsForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.ticket = ticket
            new_form.save()
            ticket.review_done = True
            ticket.save()
            return redirect('home_page')
    form_review = ReviewsForm()
    context = {
        'ticket': ticket,
        'form_review': form_review,
    }
    context['theme'] = get_object_or_404(UserTheme, user=request.user)
    return render(request, 'review/review_requested.html', context)

@login_required(login_url='/login/')
def edit_review(request, id):
    review = get_object_or_404(Review, id=id)
    if review.user == request.user:
        if request.method == "POST":
            form = ReviewsForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('review_list')
        form = ReviewsForm(instance=review)
        
        context = {
        'form': form,
        'review': review,
        }
        if request.user.is_authenticated:
            context['theme'] = get_object_or_404(UserTheme, user=request.user)
        return render(request, 'review/edit_review.html', context)
    else:
        return redirect('ticket_list')

@login_required(login_url='/login/')
def delete_review(request, id):
    review = get_object_or_404(Review, id=id)
    review.ticket.review_done = False
    review.ticket.save()
    if review.user == request.user:
        review.delete()
    return redirect('review_list')


# View about Ticket
@login_required(login_url='/login/')
def ticket_list(request):
    tickets = Ticket.objects.all()
    context = {
        'tickets': tickets
    }
    if request.user.is_authenticated:
        context['theme'] = get_object_or_404(UserTheme, user=request.user)
    return render(request, 'ticket/ticket_list.html', context)

@login_required(login_url='/login/')
def ticket_detail(request, id: int):
    ticket = get_object_or_404(Ticket, id=id)
    reviews = Review.objects.filter(ticket=ticket)
    context = {
        'ticket': ticket,
        'reviews': reviews,
        }
    if request.user.is_authenticated:
        context['theme'] = get_object_or_404(UserTheme, user=request.user)
    return render(request, 'ticket/ticket_detail.html', context)

@login_required(login_url='/login/')
def add_ticket(request):
    if request.method == "POST":
        form = TicketsForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('ticket_list')
    form = TicketsForm()
    context = {
        'form': form
    }
    if request.user.is_authenticated:
        context['theme'] = get_object_or_404(UserTheme, user=request.user)
    return render(request, 'ticket/add_ticket.html', context)

@login_required(login_url='/login/')
def edit_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    if ticket.user == request.user:
        if request.method == "POST":
            form = TicketsForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                return redirect('ticket_list')
        form = TicketsForm(instance=ticket)
        
        context = {
        'form': form,
        'ticket': ticket,
        }
        if request.user.is_authenticated:
            context['theme'] = get_object_or_404(UserTheme, user=request.user)
        return render(request, 'ticket/add_ticket.html', context)
    else:
        return redirect('ticket_list')

@login_required(login_url='/login/')
def delete_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    if ticket.user == request.user:
        ticket.delete()
    return redirect('ticket_list')


# View about Author
@login_required(login_url='/login/')
def author_list(request):
    authors = User.objects.all()
    for author in authors:
        author.nb_post_review = len(Review.objects.filter(user=author))
        all_note = Review.objects.filter(user=author)
        if len(all_note) > 0:
            author.moy_review = round(sum([x.rating for x in all_note]) / len(all_note), 1)
        else:
            author.moy_review = "null"
    follows = UserFollows.objects.filter(user=request.user)
    follows = [follow.followed_user for follow in follows]
    for author in authors:
        author.subscribe = True if author in follows else False
    context = {
        'authors': authors,
        'follows': follows,
    }
    if request.user.is_authenticated:
        context['theme'] = get_object_or_404(UserTheme, user=request.user)
    return render(request, 'author/author_list.html', context)

@login_required(login_url='/login/')
def author_detail(request, id: int):
    author = get_object_or_404(User, id=id)
    reviews = Review.objects.filter(user=author)
    context = {
        'author': author,
        'reviews': reviews,
        }
    if request.user.is_authenticated:
        context['theme'] = get_object_or_404(UserTheme, user=request.user)
    return render(request, 'author/author_detail.html', context)

