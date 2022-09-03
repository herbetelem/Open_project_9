from django import forms
from django.contrib.auth.models import User
from .models import Review, Ticket

class ReviewsForm(forms.ModelForm):
    headline = forms.CharField(label="Headline", max_length=250, help_text='', required=True,
                                widget=forms.TextInput(attrs={"class":"form-control", "id":"headline", "type":"text", "placeholder":"Headline", "data-sb-validations":"required"}))
    CHOICES = [('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]
    rating = forms.CharField(label='Rating', widget=forms.RadioSelect(choices=CHOICES, attrs={'class':'form_radio'}), required=True,)
    body = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':'3', 'class':'form-control', 'id':'body'}))
    class Meta:
        model = Review
        fields = "__all__"
        exclude = ('user', 'time_created', 'ticket', 'id')

class TicketsForm(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=250, help_text='', required=True,
                                widget=forms.TextInput(attrs={"class":"form-control", "id":"title", "type":"text", "placeholder":"Title", "data-sb-validations":"required"}))
    author = forms.CharField(label="Author", required=True,
                                widget=forms.TextInput(attrs={"class":"form-control", "id":"author", "type":"int", "placeholder":"Author", "data-sb-validations":"required"}))
    description = forms.CharField(widget=forms.Textarea(attrs={'name':'description', 'rows':'3', 'class':'form-control', 'id':'description'}))
    
    image = forms.FileField()

    class Meta:
        model = Ticket
        fields = "__all__"
        exclude = ('user', 'time_created')
