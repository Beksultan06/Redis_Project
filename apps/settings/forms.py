from django import forms
from apps.telegram.models import Telegram

class TelegramForm(forms.ModelForm):
    class Meta:
        model = Telegram
        fields = [ 'username', 'name', 'email', 'message']