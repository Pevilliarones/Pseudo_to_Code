# BAŞLA
# Onaylanmamış kullanıcıları içeren bir liste oluştur.
# Onaylanmış kullanıcıları saklamak için boş bir liste oluştur.

unconfirmed_users = ["Gencer", "Ali", "Şeyma", "Ege"]

confirmed_users = []

# Onaylanmamış kullanıcı listesi boşalana kadar döngüyü çalıştır:
#     - Listenin sonundaki kullanıcıyı al ve listeden çıkar.
#     - Kullanıcının doğrulandığını ekrana yazdır.
#     - Kullanıcıyı onaylanmış kullanıcılar listesine ekle.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Kullanıcı doğrulanıyor.. {current_user.title()}")
    print(f"{current_user.title()} başarıyla doğrulandı!")
    confirmed_users.append(current_user)

# "Aşağıdaki kullanıcılar onaylanmıştır:" mesajını ekrana yazdır.
print("Aşağıdaki kullanıcılar onaylanmıştır: ")
for confirmed_user in confirmed_users:
    print(f"- {confirmed_user.title()}")

# Onaylanmış kullanıcılar listesindeki her kullanıcı için:
#     - Kullanıcının adını baş harfi büyük olacak şekilde ekrana yazdır.
#BİTİR