import requests
import time
import winsound #sadece windows da çalışır

coin_adi = input("Alarm kurmak istediğiniz coinin ismini giriniz: ").lower().strip()
hedef_fiyat = float(input("Alarm kurulacak olan fiyat (USD): "))

def fiyat_kontrol():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_adi,
        "vs_currencies": "usd"
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        return data[coin_adi]["usd"]
    except:
        print("Veri alınırken hata oluştu.")
        return None

ilk_fiyat = fiyat_kontrol()
if ilk_fiyat is not None:
    print(f"{coin_adi.capitalize()}'nin şu anki fiyatı: {ilk_fiyat} USD")

while True:
    mevcut_fiyat = fiyat_kontrol()
    if mevcut_fiyat is not None and mevcut_fiyat >= hedef_fiyat:
        winsound.Beep(1000, 1000)
        print(f"{coin_adi} {hedef_fiyat} fiyatının üzerine çıktı ve şu anki fiyatı: ({mevcut_fiyat} USD)")
        break
    time.sleep(60)
