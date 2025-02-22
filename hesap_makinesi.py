# BAŞLA

# 1️⃣ Kullanıcıdan iki sayı al.
#    - Kullanıcıdan birinci sayıyı al.
#    - Kullanıcıdan ikinci sayıyı al.
#    - Eğer kullanıcı geçersiz bir giriş yaparsa hata ver ve tekrar denemesini iste.

# 2️⃣ Kullanıcıya yapmak istediği işlemi sor.
#    - Kullanıcıya toplama (+), çıkarma (-), çarpma (*) ve bölme (/) seçeneklerini göster.
#    - Kullanıcı "exit" yazarsa programdan çık.

# 3️⃣ Kullanıcının seçtiği işlemi gerçekleştir.
#    - Eğer işlem "+", iki sayıyı topla ve sonucu ekrana yazdır.
#    - Eğer işlem "-", birinci sayıdan ikinci sayıyı çıkar ve sonucu yazdır.
#    - Eğer işlem "*", iki sayıyı çarp ve sonucu yazdır.
#    - Eğer işlem "/", önce ikinci sayının sıfır olup olmadığını kontrol et.
#       - Eğer ikinci sayı sıfır değilse bölme işlemi yap ve sonucu yazdır.
#       - Eğer ikinci sayı sıfırsa hata mesajı göster ve tekrar giriş iste.
#    - Eğer kullanıcı geçersiz bir işlem girerse hata mesajı göster ve tekrar işlem girmesini iste.

# 4️⃣ Kullanıcı çıkış yapana kadar 1. adımdan itibaren işlemi tekrar et.

# BİTİR


while True:
    num1_input = input("Birinci sayıyı giriniz (veya çıkmak için 'exit' yazın): ")
    if num1_input.lower() == "exit":
        print("Hesap makinesi kapatılıyor.")
        break

    num2_input = input("İkinci sayıyı giriniz (veya çıkmak için 'exit' yazın): ")
    if num2_input.lower() == "exit":
        print("Hesap makinesi kapatılıyor.")
        break

    num1 = float(num1_input)
    num2 = float(num2_input)

    işlem = input("Yapmak istediğiniz işlemi girin (+, -, *, /) veya çıkmak için 'exit' yazın: ")

    if işlem.lower() == "exit":
        print("Hesap makinesi kapatılıyor.")
        break

    elif işlem == "+":
        print(f"Sonuç: {num1} + {num2} = {num1 + num2}\n")

    elif işlem == "-":
        print(f"Sonuç: {num1} - {num2} = {num1 - num2}\n")

    elif işlem == "*":
        print(f"Sonuç: {num1} * {num2} = {num1 * num2}\n")

    elif işlem == "/":
        if num2 != 0:
            print(f"Sonuç: {num1} / {num2} = {num1 / num2}\n")
        else:
            print("Hata! Bir sayı sıfıra bölünemez.\n")

    else:
        print("Geçersiz işlem! Lütfen tekrar deneyin.\n")
