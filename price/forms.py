from django import forms

CHOICES_PRODUCT = [('potato', "Картошка"), ("cabbage", "Капуста")]
CHOICES_CITY = [('Москва', "Москва"), ("Санкт-Петербург", "Санкт-Петербург")]


class PriceForm(forms.Form):
    product = forms.ChoiceField(label='Товар', choices=CHOICES_PRODUCT, widget=forms.Select)
    cityfrom = forms.ChoiceField(label='Откуда:', choices=CHOICES_CITY, widget=forms.Select)
    cityto = forms.ChoiceField(label='Куда:', choices=CHOICES_CITY, widget=forms.Select)
    weight = forms.IntegerField(label='Вес(тонны):', initial=20000)
    nds = forms.BooleanField(label='С НДС?', required=False)
    with_nds = forms.BooleanField(label='Без НДС?', required=False)
    nal = forms.BooleanField(label='Оплата наличными?', required=False)
    beznal = forms.BooleanField(label='Оплата картой?', required=False)