from django import forms
from .models import Review
from django.contrib.auth.models import User

class ReviewForm(forms.ModelForm):
    '''
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        if self.request:
            self.user = self.request.user
        else:
            self.user = None'''

    class Meta:
        model = Review
        fields = ('user','rating','text')

    '''
    def clean(self):
        cleaned_data = super().clean()
        user = self.user

        return cleaned_data
    
    def save(self):
        if self.user.is_authenticated:
            pass
'''