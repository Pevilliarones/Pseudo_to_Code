# 1️⃣ Kullanıcıdan kaç puanı olduğunu sor
#    - "How many points are on your card?" yazdır
#    - Girdiyi al ve sayıya çevir (float olarak sakla)
girdi = float(input("How many points are on your card? "))
# 2️⃣ Bonus hesaplama:
#    - Eğer puan 100'den küçükse:
#        - Bonus yüzde 10 (%10)
#        - Yeni puanı (puan * 1.10) olarak hesapla
#    - **Aksi halde** (100 veya daha fazla puan varsa):
#        - Bonus yüzde 15 (%15)
#        - Yeni puanı (puan * 1.15) olarak hesapla
if girdi < 100:
    print ("Your bonus is 10 %")
    girdii = girdi * 1.10
    print (f"You now have {girdii} points")
else:
    print("Your bonus is 15 %")
    yenigirdi = girdi * 1.15
    print(f"You now have {yenigirdi} points")

# 3️⃣ Sonuçları ekrana yazdır:
#    - "Your bonus is X %" → Bonus yüzdesini yazdır
#    - "You now have Y points" → Yeni puanı yazdır