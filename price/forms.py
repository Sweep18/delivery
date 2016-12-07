from django import forms

CHOICES_PRODUCT = [('potato', "Картошка"), ("cabbage", "Капуста")]
CHOICES_CITY = [('Москва', "Москва"), ("Санкт-Петербург", "Санкт-Петербург")]
WEIGHTS = [(1500, "1,5 т"), (3000, "3 т"), (5000, "5 т"), (10000, "10 т"), (20000, "20 т")]


class PriceForm(forms.Form):
    product = forms.ChoiceField(label='Товар', choices=CHOICES_PRODUCT, widget=forms.Select)
    cityfrom = forms.ChoiceField(label='Откуда:', choices=CHOICES_CITY, widget=forms.Select)
    cityto = forms.ChoiceField(label='Куда:', choices=CHOICES_CITY, widget=forms.Select)
    weight = forms.ChoiceField(label='Вес(тонны):', choices=WEIGHTS, widget=forms.Select, initial=20000)
    nds = forms.BooleanField(label='С НДС?', required=False)
    with_nds = forms.BooleanField(label='Без НДС?', required=False)
    nal = forms.BooleanField(label='Оплата наличными?', required=False)
    beznal = forms.BooleanField(label='Оплата картой?', required=False)