from django.shortcuts import render
import urllib.request
import json

# Create your views here.

def index(request):
    if request.method == "POST":
        from_currency = request.POST['from_currency']
        to_currency = request.POST['to_currency']
        amount = float(request.POST['amount'])
        res = urllib.request.urlopen('https://v6.exchangerate-api.com/v6/e9902716f3cbd8088c0df394/pair/' + from_currency + '/' + to_currency).read()
        json_data = json.loads(res)
        conversion_rates =  json_data['conversion_rate']
        converted_amount = amount*conversion_rates

        data = {
            'from_currency' : from_currency.upper(),
            'to_currency' : to_currency.upper(),
            'amount' : amount,
            'conversion_rates' : conversion_rates,
            'converted_amount' : converted_amount,
        }
    else: 
        data = {}
        converted_amount=''

    return render(request, 'index.html',{'data':data})



