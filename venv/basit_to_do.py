# 📝 1️⃣ Boş bir liste oluştur  
# Kullanıcının notlarını saklamak için boş bir liste kullan  

# 📝 2️⃣ While döngüsünü başlat  
# Program sürekli çalışsın, kullanıcı çıkış yapana kadar devam et  

notlar = []
    # 🟢 **1. BLOK: Kullanıcıya menüyü göster**  
    # Yazdır:  
    # 📌 Not Defteri Uygulaması  
    # 1. Yeni not ekle  
    # 2. Notları listele  
    # 3. Çıkış  
while True:
    print("\n📌 Not Defteri Uygulaması")
    print("1. Yeni not ekle")
    print("2. Notları listele")
    print("3. Çıkış")
# 🟢 **2. BLOK: Kullanıcıdan giriş al**  
# Kullanıcıdan bir seçim yapmasını iste  
    seçim = int(input("Bir seçim yapın: "))
# 🟢 **3. BLOK: Çıkış kontrolü**  
# Eğer kullanıcı 3'ü seçerse:  
#     "Çıkılıyor..." mesajı yazdır  
#     Döngüyü durdur  
    if seçim == 3:
        print ("Çıkılıyor...")
        break
# 🟢 **4. BLOK: Kullanıcının seçimine göre işlemleri gerçekleştir**  
# Eğer kullanıcı 1’i seçerse → Yeni not ekleme bloğuna git  
#     Kullanıcıdan not al  
#     Listeye ekle  
#     "Not eklendi!" mesajı göster  
    elif seçim == 1:
        yeninot = input("Notunuzu buraya giriniz: ")
        notlar.append(yeninot)
        print("Not eklendi!")
# Eğer kullanıcı 2’yi seçerse → Notları listeleme bloğuna git  
#     Eğer liste boşsa:  
#         "Hiç not yok!" mesajı göster  
#     Aksi halde tüm notları sırayla ekrana yazdır 
    # Eğer kullanıcı 2’yi seçerse → Notları listele
    elif seçim == 2:
        if not notlar:  # Eğer liste boşsa
            print("Hiç not yok!")
        else:
            for doc in notlar:
                print(doc)
        print("Program sonlandırılıyor...")
        break