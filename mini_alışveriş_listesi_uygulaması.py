# 1️⃣ Boş bir alışveriş listesi oluştur (liste kullan)
alışveriş = []
# 2️⃣ While döngüsü başlat (Kullanıcı "exit" yazana kadar çalışacak)
#     - Kullanıcıdan ürün ismi al (input ile)
#     - Eğer "exit" yazarsa döngüyü kır (break)
#     - Eğer yazdığı şey "exit" değilse, listeye ekle (append ile)
while True:
    isimal = input("Ürünün ismini yazınız?\n")
    if isimal == "exit":
        break
    else:
        alışveriş.append(isimal)

for liste in alışveriş:
    print (f"Alınacaklar {liste}")
    
if not alışveriş:
    print("Alışveriş listenizde ürün yok.")