from django import forms
from django.core.exceptions import ValidationError
from eventex.subscriptions.models import Subscription

def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas número', 'digits')
    
    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números.', 'length')

class SubscriptionForm(forms.ModelForm):
    name = forms.CharField(label="Nome")
    cpf = forms.CharField(label="CPF", validators=[validate_cpf])
    email = forms.EmailField(label="Email", required=False)
    phone = forms.CharField(label="Telefone", required=False)

    class Meta:
        model = Subscription
        fields = 'name', 'cpf','email', 'phone'

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)
    
    def clean(self):
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone.')
        return self.cleaned_data
