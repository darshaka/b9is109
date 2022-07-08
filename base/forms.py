from django.forms import ModelForm
from .models import NewsArtical
from django.contrib.auth.models import User

class NewsPaperForm(ModelForm):
    class Meta:
        model = NewsArtical
        fields = '__all__'
        exclude = ['newsAdmin', 'subscribers']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        
        # ['username', 'email', 'password', 'is_superuser']