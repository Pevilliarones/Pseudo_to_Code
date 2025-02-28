# 1️⃣ Kullanıcıdan ilk sayıyı al ve bir değişkene kaydet.
#     - Kullanıcının sayıyı doğru girdiğinden emin olmak için tam sayı (int) olarak kaydet.
num1 = int(input("Bir sayı gir: "))

# 2️⃣ Kullanıcıdan ikinci sayıyı al ve bir değişkene kaydet.
#     - Yine tam sayı (int) olarak kaydet.
num2 = int(input("Bir sayı daha gir: "))
# 3️⃣ Kullanıcıdan işlem türünü al.
#     - Kullanıcı "add", "multiply" veya "subtract" yazabilir.
#     - Küçük/büyük harf farkını önlemek için girilen metni küçük harfe çevir.
toplama = num1 + num2
çarpma = num1 * num2
çıkarma = num1 - num2

işlem = input("Yapmak istediğiniz işlem nedir? add - multiply - subtract ")
# 4️⃣ Eğer işlem "add" ise:
#     - İlk sayı ile ikinci sayıyı topla.
#     - Sonucu ekrana şu şekilde yazdır: "10 + 17 = 27"
if işlem == "add":
    print(f"{num1} + {num2} = {toplama}")
# 5️⃣ Eğer işlem "multiply" ise:
#     - İlk sayı ile ikinci sayıyı çarp.
#     - Sonucu ekrana şu şekilde yazdır: "4 * 6 = 24"
elif işlem == "multiply":
    print(f"{num1} * {num2} = {çarpma}")
# 6️⃣ Eğer işlem "subtract" ise:
#     - İlk sayıdan ikinci sayıyı çıkar.
#     - Sonucu ekrana şu şekilde yazdır: "4 - 6 = -2"
elif işlem == "subtract":
    print(f"{num1} - {num2} = {çıkarma}")
# 7️⃣ Eğer işlem bunlardan biri değilse:
#     - Program hiçbir şey yazdırmamalı (boş bırakılmalı).
