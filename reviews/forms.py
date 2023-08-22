from django import forms

from .models import Publisher, Review, Book

class SearchForm(forms.Form):
    search= forms.CharField(min_length=3, required=False)
    search_in = forms.ChoiceField(choices=(("title", "Title"), 
                                           ("contributor", "Contributor"))
                                  , required=False)
    

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
    
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["date_edited", "book"]

    rating = forms.IntegerField(min_value=0, max_value=5)
    
class BookMediaForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ('cover', 'sample')
