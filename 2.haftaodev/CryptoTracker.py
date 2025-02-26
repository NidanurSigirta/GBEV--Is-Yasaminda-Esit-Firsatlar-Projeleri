import time
import requests
from datetime import datetime
from uuid import uuid4
from pprint import pprint

BASE_URL = "https://api.coingecko.com/api/v3"
crypto_list = {}

def get_crypto_price(crypto_id):
    """Kripto para fiyatını CoinGecko API'sinden alıyoruz"""
    url = f"{BASE_URL}/simple/price"
    params = {
        "ids": crypto_id,
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Hata kodu:", response.status_code)
        return None

def get_historical_price(crypto_id, days):
    """Kriptonun geçmiş fiyatlarını getirir"""
    url = f"{BASE_URL}/coins/{crypto_id}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": str(days),
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if "prices" in data:
            prices = data["prices"]
            print(f"{crypto_id} için son {days} günün fiyatları:")
            for price in prices:
                timestamp = price[0] / 1000  # milisaniyeden saniyeye dönüşüm
                date_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                print(f"Tarih: {date_time} - Fiyat: ${price[1]:.2f}")
        else:
            print("Veri alınamadı, 'prices' bilgisi yok.")
    else:
        print("Geçmiş veriler alınamadı!")
        print(f"Hata kodu: {response.status_code}")
        if response.status_code == 429:
            print("API istek limiti aşıldı. Lütfen birkaç saniye bekleyin ve tekrar deneyin.")
            time.sleep(10)  # 10 saniye bekleyin

# CRUD işlemleri
while True:
    process = input('Bir işlem türü girin (create, list, update, delete, historical): ')

    match process:
        case 'create':
            crypto_id = str(uuid4())
            crypto_data = get_crypto_price(input('Kripto para ismi: '))
            if crypto_data:
                crypto_list[crypto_id] = {
                    'name': input('Kripto para adı: '),
                    'price': crypto_data.get(list(crypto_data.keys())[0])['usd']
                }
                pprint(crypto_list)
            else:
                print('Kripto para eklenemedi.')

        case 'list':
            pprint(crypto_list)

        case 'update':
            crypto_id = input('Id girin: ')
            if crypto_id in crypto_list:
                new_price_data = get_crypto_price(crypto_list[crypto_id]['name'])
                if new_price_data:
                    crypto_list[crypto_id]['price'] = new_price_data.get(list(new_price_data.keys())[0])['usd']
                    print(f"{crypto_list[crypto_id]['name']} güncellendi: ${crypto_list[crypto_id]['price']}")
                    pprint(crypto_list)
                else:
                    print('Fiyat güncellenemedi.')
            else:
                print('Kripto para bulunamadı.')

        case 'delete':
            crypto_id = input('Id girin: ')
            if crypto_id in crypto_list:
                del crypto_list[crypto_id]
                print(f"{crypto_id} listeden silindi.")
                pprint(crypto_list)
            else:
                print('Kripto para bulunamadı.')

        case 'historical':
            crypto_id = input('Kripto para ismi: ')
            days = input('Kaç gün geriye dönmek istersiniz: ')
            get_historical_price(crypto_id, days)

        case _:
            print('Geçersiz işlem türü! Lütfen geçerli bir işlem girin.')

