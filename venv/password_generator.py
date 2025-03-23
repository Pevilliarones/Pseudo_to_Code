# 🔐 Şifre Oluşturma Programı - ZOR Versiyon PSEUDO KOD 🔐
# Amaç: Kullanıcının istediği sayıda harf, sembol ve rakam içeren,
# ama KARMA (RANDOM) sırayla dizilmiş bir şifre oluşturmak

# 1️⃣ Modülleri ve listeleri hazırla
# - random modülünü import et
# - letters listesi → küçük ve büyük harfler olacak
# - symbols listesi → özel karakterler (ör: !, #, $, %, &, *, +)
# - numbers listesi → '0' - '9' arası rakamlar

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# 2️⃣ Kullanıcıdan bilgileri al
# - Kaç harf istiyorsun? → num_letters
# - Kaç sembol istiyorsun? → num_symbols
# - Kaç rakam istiyorsun? → num_numbers

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# 3️⃣ Boş bir password_list başlat
# - Liste kullanıyoruz çünkü içine karakterleri ekleyip KARIŞTIRACAĞIZ
password_list = []
# 4️⃣ Harfleri ekle
# - num_letters kadar döngü başlat:
#   → random.choice(letters) ile rastgele bir harf seç
#   → Seçilen harfi password_list'e ekle (append)
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
# 5️⃣ Sembolleri ekle
# - num_symbols kadar döngü başlat:
#   → random.choice(symbols) ile rastgele sembol seç
#   → password_list'e ekle
for char in range (0, nr_symbols):
    password_list.append(random.choice(symbols))
# 6️⃣ Rakamları ekle
# - num_numbers kadar döngü başlat:
#   → random.choice(numbers) ile rastgele rakam seç
#   → password_list'e ekle
for char in range (0, nr_numbers):
    password_list.append(random.choice(numbers))
# 7️⃣ Listeyi karıştır
# - random.shuffle(password_list) kullan
# - Böylece harfler, semboller, rakamlar karışır, rastgele dağılır
random.shuffle(password_list)
# 8️⃣ Listeyi stringe çevir
# - ''.join(password_list) → tüm karakterleri birleştir
# - Ortaya tam bir şifre çıkar
# 9️⃣ Şifreyi yazdır
# - Ekrana yaz → Kullanıcı güçlü ve rastgele karıştırılmış şifreyi görsün
password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")

# ✅ ÖRNEK:
# Kullanıcı der ki:
# Kaç harf? 4
# Kaç sembol? 2
# Kaç rakam? 3
#
# Çıktı → x$g3Y9*a  (Dikkat: Hepsi karışık, sıralı değil!)
