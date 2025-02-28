# 1️⃣ Kullanıcıdan yarının hava durumu tahminini al  
#    - "What is the weather forecast for tomorrow?" yazdır  
#    - Kullanıcıdan sıcaklık bilgisini al ve sayıya çevir (int veya float olarak sakla)  
hava_durumu = int(input("What is the weather forecast for tomorrow? Temperature: "))
# 2️⃣ Kullanıcıya "Will it rain (yes/no)?" sorusunu sor  
#    - Girdiyi küçük harfe çevir ki "Yes", "YES", "yEs" gibi girişler sorun çıkarmasın  
rain = input("Will it rain? ").lower()
# 3️⃣ Temel kıyafet önerisini yazdır  
#    - "Wear jeans and a T-shirt"  
print ("Wear jeans and a T-shirt")
# 4️⃣ Sıcaklık koşullarına göre ekstra öneriler ekle  
#    - Eğer sıcaklık 10 ile 20°C arasında ise:  
#        - "I recommend a jumper as well" yazdır  
#    - Eğer sıcaklık 5 ile 10°C arasında ise:  
#        - "I recommend a jumper as well" yazdır  
#        - "Take a jacket with you" yazdır  
#    - Eğer sıcaklık 5°C’den düşükse:  
#        - "I recommend a jumper as well" yazdır  
#        - "Take a jacket with you" yazdır  
#        - "Make it a warm coat, actually" yazdır  
#        - "I think gloves are in order" yazdır  
if 10 <= hava_durumu <= 20:  
    print("I recommend a jumper as well")
elif 5 <= hava_durumu <= 10:
    print("I recommend a jumper as well")
    print("Take a jacket with you")
elif hava_durumu < 5:
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")


# 5️⃣ Yağmur durumunu kontrol et  
#    - Eğer yağmur yağacaksa ("yes" cevabı verilmişse):  
#        - "Don't forget your umbrella!" yazdır  
if rain == "yes":
    print("Don't forget your umbrella!")