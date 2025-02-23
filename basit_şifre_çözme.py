çözme_sözlüğü = {
    "@": "a",
    "8": "b",
    "3": "e",
    "1": "g",
    "2": "e",
    "3": "n",
    "4": "c",
    "6": "r"
}

while True:
    kelime = input("Şifreli kelimenizi giriniz. ")
    çözülmüş_kelime = ""
    
    
    for harf in kelime:
        if harf in çözme_sözlüğü:
            çözülmüş_kelime += çözme_sözlüğü[harf]
        else:
            çözülmüş_kelime += harf

    print("Çözülen kelime: ", çözülmüş_kelime)