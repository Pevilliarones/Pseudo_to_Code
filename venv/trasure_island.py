print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Hazine adasına hoşgeldiniz!")
print("Göreviniz hazine sandığını bulmak.")

secim1 = input ("Bir yol ayrımındasın, nereye gitmek istiyorsun? 'sol' veya 'sağ' yaz.").lower()

if secim1 == "sol":
    print("Bir göle geldin. Gölde bir ada var.")
    secim2 = input("Tekneyi beklemek için 'bekle' yaz. Yüzerek geçmek için 'yüz' yaz.").lower()

    if secim2 == "bekle":
        print("Adaya sağ salim ulaştın.")
        secim3 = input("Önünde üç kapı var: Kırmızı, Sarı ve Mavi. Hangi kapıyı seçiyorsun?").lower()
        if secim3 == "kırmızı":
            print("Burası alevlerle dolu bir oda! OYUN BİTTİ.")

        elif secim3 == "sarı":
            print("Tebrikler! Hazineyi buldun! OYUNU KAZANDIN!")

        elif secim3 == "mavi":
            print("Canavarlarla dolu bir odaya girdin! OYUN BİTTİ.")

        else:
            print("Böyle bir kapı yok! OYUN BİTTİ.")

    else:
        print("Saldırgan bir balık sana saldırdı! OYUN BİTTİ.")

else:
    print("Bir çukura düştün! OYUN BİTTİ!")