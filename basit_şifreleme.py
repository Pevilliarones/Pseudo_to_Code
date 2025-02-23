sözlük = {
    "a": "@", "b": "8", "e": "3"
}

while True:
    kelime = input("Bir kelime giriniz: ")
    şifrelenmiş_kelime = ""
    
    for harf in kelime:
        if harf in sözlük:
            şifrelenmiş_kelime += sözlük[harf]  # Harfi değiştir ve ekle
        else:
            şifrelenmiş_kelime += harf  # Değiştirmeden ekle
    
    print("Şifrelenmiş Kelime:", şifrelenmiş_kelime)
