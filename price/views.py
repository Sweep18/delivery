from django.shortcuts import render
from .forms import PriceForm
import requests
from geopy.distance import vincenty
from geopy.geocoders import Yandex


def price(request):
    if request.method == 'POST':
        form = PriceForm(request.POST)
        if form.is_valid():
            url_price = 'https://groozgo.ru/api/order/calc_price'
            url_drive = 'https://groozgo.ru/api/order/find_drivers'

            headers = {'Content-Type': 'application/json; charset=utf-8',
                       'X-Requested-With': 'XMLHttpRequest'}

            cityfrom = form.cleaned_data.get('cityfrom', None)
            cityto = form.cleaned_data.get('cityto', None)
            weight = form.cleaned_data.get('weight', None)
            nds = form.cleaned_data.get('nds', None)
            nal = form.cleaned_data.get('nal', None)
            from_value = "Россия, " + str(cityfrom)
            to_value = "Россия, " + str(cityto)

            geolocator = Yandex()
            loc_from = geolocator.geocode(str(cityfrom))
            loc_to = geolocator.geocode(str(cityto))
            loc_from_coord = (loc_from.latitude, loc_from.longitude)
            loc_to_coord = (loc_to.latitude, loc_to.longitude)
            distance = vincenty(loc_from_coord, loc_to_coord).meters

            data_price = {"distance": distance, "weight": str(weight), "from_administrative_area": cityfrom,
                          "to_administrative_area": cityto, "mkad_distance": 23813.79,
                          "is_refrigerator": False, "is_isotherm": False, "is_insurance": False,
                          "insurance_sum": 0, "porters_count": "0", "destination_points": {},
                          "destination_points_amount": 0,
                          "is_documents_back": False, "is_online_tracking": False, "back_doc_address": "",
                          "from_value": from_value, "to_value": to_value}

            price_temp = requests.post(url_price, json=data_price, headers=headers)
            price = round(price_temp.json()['totalPrice'])

            data_drive = {"payment_info": {"with_nds": nds, "without_nds": False, "cash": nal, "cashless": True},
                          "services": {"isotherm": False, "refrigerator": False}, "administrative_area_from": cityfrom,
                          "administrative_area_to": cityto, "cargo_weight": str(weight)}

            drive = requests.post(url_drive, json=data_drive, headers=headers)
            return render(request, 'ok.html', {'price': price, 'drive': drive.text})
    else:
        form = PriceForm()
    return render(request, 'main.html', {'form': form})