#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Döngüde Felsefe Yapan Bot
Gerçekten çalışır. Gerçekten anlamsızdır.
"""

import random
import time
import base64

# Gizli not (asla çalıştırma, sadece sakla)
GIZLI = base64.b64decode("SGVyIHBhcnRpIGF5bsSxZMSxciwgZ2VyZ2VrIHNlaW1lbiBheW7EscSHLCBhbWEgaGnDpyBiaXJpIGFubGFzaWxtYXogYXluxLEgZGVnaWxkaXIu").decode("utf-8")

def felsefe_uret():
    konular = [
        "varoluş", "zaman", "boşluk", "çay", "klavye", "internet", "sessizlik",
        "gürültü", "bekleme", "anlamsızlık", "anlam", "kedi", "ekran", "uyku"
    ]
    eylemler = [
        "sadece bir illüzyondur", "asla bitmez", "kendini yutar", "seni izler",
        "hiç var olmamıştır", "her an yeniden doğar", "senin yüzünden vardır"
    ]
    sonuclar = [
        "Bu yüzden çay iç.", "Ama yine de bekle.", "Soru yanlış.",
        "Cevap yok çünkü soru da yok.", "Şimdi uyu."
    ]
    
    konu = random.choice(konular)
    eylem = random.choice(eylemler)
    sonuc = random.choice(sonuclar)
    
    return f"{konu.capitalize()} {eylem}. {sonuc}"

def main():
    print("=== Sonsuz Döngüde Felsefe Yapan Bot Başlatıldı ===")
    print("Durdurmak için Ctrl+C. Durdurmazsan sonsuza kadar devam eder.\n")
    
    sayac = 0
    while True:
        print(felsefe_uret())
        time.sleep(random.uniform(1.5, 4.0))
        sayac += 1
        
        if sayac % 7 == 0:
            print("\n>>> Anladın mı? <<<")
            print("(Cevabınız dinlenmiyor. Zaten önemli değil.)\n")
            time.sleep(2)
        
        if sayac % 23 == 0:
            print("\n[Sistem notu: Hala buradasın. İlginç.]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBot durduruldu. Ama düşünceler durmadı.")
        print("Görüşürüz. Belki.")
