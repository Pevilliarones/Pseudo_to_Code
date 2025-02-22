# BAŞLA

# 1️⃣ Doğru şifreyi belirle.
#    - Örneğin: "1234"

# 2️⃣ Kullanıcıdan şifre girmesini iste.

# 3️⃣ Kullanıcı çıkış yapmak isterse:
#    - Eğer kullanıcı "exit" yazarsa, programdan çık.

# 4️⃣ Girilen şifreyi kontrol et:
#    - Eğer şifre doğruysa:
#        - "Giriş başarılı!" mesajını göster.
#        - Programı bitir.

#    - Eğer şifre yanlışsa:
#        - "Hatalı şifre! Tekrar deneyin." mesajını göster.
#        - Kullanıcıdan tekrar şifre girmesini iste.

# 5️⃣ Kullanıcı doğru şifre girene kadar 4. adımı tekrar et.

# BİTİR

prompt = "Bir şifre girin. 'exit' yazarsanız programdan çıkacaksınız. "
şifre = "1234"

while True:
    şifre_gir = input(prompt)
    if şifre_gir == şifre:
        print("Giriş başarılı! Hoş geldiniz!")
        break
    elif şifre_gir.lower()== "exit":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Hatalı şifre! Tekrar deneyin.")