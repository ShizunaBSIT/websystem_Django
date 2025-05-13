from django.shortcuts import reverse

class LoginRequired(Exception):
    def __init__(self, *args, **kwargs):
        self.redirect_url = reverse('loginformpage')  # Assuming you named your login URL 'login'
        super().__init__(*args, **kwargs)