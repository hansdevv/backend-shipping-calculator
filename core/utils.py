import requests
from django.conf import settings

def cek_ongkir(asal_id, tujuan_id, berat, kurir):
    url = f"{settings.RAJAONGKIR_BASE_URL}/calculate/domestic-cost"
    headers = {
        'key': settings.RAJAONGKIR_API_KEY,
        'content-type': 'application/x-www-form-urlencoded'
    }
    payload = {
        'origin': asal_id,
        'destination': tujuan_id,
        'weight': berat,
        'courier': kurir
    }

    response = requests.post(url, headers=headers, data=payload)
    try:
        return response.json()
    except Exception:
        return {
            "error": "Gagal parse JSON dari RajaOngkir",
            "status_code": response.status_code,
            "raw_response": response.text
        }

def search_domestic_destination(search, courier=None):
    url = f"{settings.RAJAONGKIR_BASE_URL}/destination/domestic-destination"
    headers = {
        'key': settings.RAJAONGKIR_API_KEY,
        'content-type': 'application/json'
    }
    params = {"search": search}
    if courier:
        params["courier"] = courier

    response = requests.get(url, headers=headers, params=params)
    return response.json()


