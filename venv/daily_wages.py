# 1️⃣ Kullanıcıdan saatlik ücreti al.
hourly = float(input("Hourly wage: "))

# 2️⃣ Kullanıcıdan kaç saat çalıştığını al.
hworked = float(input("Hours worked: "))

# 3️⃣ Kullanıcıdan hangi gün çalıştığını al ve küçük harfe çevir.
day = input("Day of the week: ").strip().lower()  

# 4️⃣ Gün kontrolü yap ve günlük ücreti hesapla.
if day == "sunday":
    daily_wage = (hourly * 2) * hworked
else:
    daily_wage = hourly * hworked

# 5️⃣ Sonucu ekrana yazdır.
print(f"Daily wages: {daily_wage:.2f} euros")
