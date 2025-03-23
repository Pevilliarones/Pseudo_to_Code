# 1️⃣ "random" modülünü içe aktar
import random
# 2️⃣ Rastgele bir sayı üret ve bir değişkene ata (1 ile 10 arasında)  👈 *İşte burada kullanacaksın!*
rastgele = random.randint(1, 10)
# 3️⃣ While döngüsü başlat (Kullanıcı doğru tahmin edene kadar çalışacak)
#     - Kullanıcıdan tahmin al (input ile)
#     - Eğer tahmin doğruysa, "Tebrikler!" mesajı yaz ve döngüyü kır (break)
#     - Eğer tahmin yanlışsa, "Tekrar dene!" mesajı ver ve tekrar tahmin al
while True:
    girdi = int(input("Bir sayı gir: "))
    if girdi == rastgele:
        print('Tebrikler!')
        break
    else:
        print("Tekrar dene")
# 4️⃣ Doğru tahmin edilince program sonlansın