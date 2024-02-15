from datetime import date, timedelta
import requests
import xml.etree.ElementTree as ET
from django.shortcuts import render



def get_current_usd(request):
    current_date = date.today()
    formatted_dates_list = []
    usd_rates_list = []
    name_rate_list = []
    valute_id_list = []

    formatted_date = current_date.strftime("%d/%m/%Y")
    API_URL = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={formatted_date}'
    response = requests.get(API_URL)
    root = ET.fromstring(response.content)

    for i in root.findall('Valute'):
        valute_id = i.get('ID')
        name_rate = i.find('Name').text
        usd_rate = float(i.find('Value').text.replace(',', '.').replace(' ', ''))
        usd_rate = round(usd_rate, 2)
        valute_id_list.append(valute_id)
        name_rate_list.append(name_rate)
        usd_rates_list.append(usd_rate)
        formatted_dates_list.append(formatted_date)

        current_date -= timedelta(days=1)
    listas = zip(formatted_dates_list, name_rate_list, valute_id_list, usd_rates_list)


    return render(request, 'get_current_usd.html', {'listas': listas, 'formatted_date':formatted_date })

