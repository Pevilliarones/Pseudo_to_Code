# Adım 1: Kullanıcıdan a, b ve c değerlerini al
# - Kullanıcıdan giriş alırken, bu girişlerin sayıya çevrildiğinden emin ol
# - Kullanıcıdan alınan değerler float (ondalıklı sayı) olacak çünkü kökler tam sayı olmayabilir
# - Kullanıcıya hangi değeri girdiğini belirgin bir şekilde göster
from math import sqrt

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

if a == 0:
    print("This is not a quadratic equation ")
    exit()
# Adım 2: Diskriminantı hesapla
# - Diskriminant formülü: D = b² - 4ac
# - Diskriminantın negatif olmayacağını biliyoruz çünkü problem bunu garanti ediyor
D = b**2 - 4*a*c
if D < 0:
    print("This equation has no real roots")
    exit()
    # Adım 3: Kökleri hesapla
    # - Formül: x1 = (-b + sqrt(D)) / (2a)
    # - Formül: x2 = (-b - sqrt(D)) / (2a)
    # - Karekök hesaplamak için math kütüphanesinden sqrt fonksiyonunu kullan
x1 = (-b + sqrt(D)) / (2 * a)
x2 = (-b - sqrt(D)) / (2 * a)

    # Adım 4: Kökleri ekrana yazdır
    # - Kullanıcıya anlaşılır şekilde çıktı ver
    # - "The roots are x1 and x2" formatında yazdır
print(f"The roots of the equation are: x1 = {x1}, x2 = {x2}")

    # Bonus: İleri seviye hata kontrolü eklenebilir
    # - Eğer a=0 girilirse, bu bir ikinci derece denklem olmaz (bunu kontrol edebiliriz)
    # - Kullanıcı hatalı giriş yaparsa hata mesajı gösterilebilir

    # Programın çalışması gereken akış:
    # 1. Kullanıcıdan a, b, c değerleri alınır
    # 2. Diskriminant hesaplanır
    # 3. İki kök hesaplanır ve ekrana yazdırılır
