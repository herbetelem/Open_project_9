from django.contrib import admin
from .models import Review, Ticket, AskReview

# Register your models here.
admin.site.register(Review)
admin.site.register(AskReview)
admin.site.register(Ticket)
