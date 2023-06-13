from django import forms

ORDER_TYPE = {
    ('Samovivos', 'Самовывоз'),
    ('Dostavka', 'Доставка'),
}
PAYMENT = {
    ('C', 'Наличными'),
}
class CheckoutForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Иван',
        'class': 'form-control',
    }))
    second_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Иванов',
        'class': 'form-control',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '+7 (123) 456 7890',
        'class': 'form-control',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'г.Ржев',
        'class': 'form-control',
    }))
    payment1 = forms.ChoiceField(choices=PAYMENT)
    telegram = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control',
    }), required=True)
    payment = forms.ChoiceField(choices=ORDER_TYPE)