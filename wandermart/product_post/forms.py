from django import forms
from .models import Review
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .exceptions import LoginRequired
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class SearchForm(forms.Form):
    query = forms.CharField(required=False, max_length=255)

class ReviewForm(forms.ModelForm):

    # Your other form fields
    '''rating = forms.IntegerField()
    text = forms.Textarea()
    user = forms.CharField(widget=forms.HiddenInput(), required=False)'''

    class Meta:
        model = Review
        fields = ('rating','text')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if self.request and not self.request.user.is_authenticated:
            raise LoginRequired("You must be logged in to submit a review.")
        return cleaned_data

    def save(self, commit=True):
        review = super().save(commit=False)
        if self.request and self.request.user.is_authenticated:
            review.user = self.request.user
        if commit:
            review.save()
        return review


#### REGISTRATION
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)


### LOGIN
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})) # Optional

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_cache = None  # For internal use by AuthenticationForm methods

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            from django.contrib.auth import authenticate
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    'Please enter a correct username and password. Note that both fields may be case-sensitive.',
                    code='invalid_login',
                )
            elif not self.user_cache.is_active:
                raise forms.ValidationError(
                    'This account is inactive.',
                    code='inactive',
                )
        return self.cleaned_data

    def get_user(self):
        return self.user_cache