# 1️⃣ Kullanıcıdan Fahrenheit cinsinden sıcaklık değeri al.
fahrenheit = float(input("Please type in a temperature (F): "))

# 2️⃣ Fahrenheit'tan Celsius'a dönüşüm formülünü uygula.
celsius = (fahrenheit - 32) * 5 / 9  # Kesin değer korunuyor!

# 3️⃣ Hesaplanan Celsius değerini ekrana yazdır.
print(f"{fahrenheit:.0f} degrees Fahrenheit equals {celsius} degrees Celsius")  


if celsius < 0:  
    print("Brr! It's cold in here!")
