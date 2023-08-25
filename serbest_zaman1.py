from datetime import datetime, timedelta, time

# Kullanıcıdan tarih girişlerini alın
tarih1_str = input("İlk tarihi girin (YYYY-MM-DD HH:MM): ")
tarih2_str = input("İkinci tarihi girin (YYYY-MM-DD HH:MM): ")

# Tarihleri datetime nesnelerine dönüştürün
tarih1 = datetime.strptime(tarih1_str, '%Y-%m-%d %H:%M')
tarih2 = datetime.strptime(tarih2_str, '%Y-%m-%d %H:%M')

# Mesai saatleri ve yemek saatlerini belirleyin
mesai_baslama = time(8, 0)           # 08:00
mesai_bitis = time(17, 30)           # 17:30
yemek_saati1_baslama = time(12, 0)   # 12:00
yemek_saati1_bitis = time(13, 0)     # 13:00
yemek_saati2_baslama = time(18, 30)  # 18:30
yemek_saati2_bitis = time(19, 30)    # 19:30
yemek_saati3_baslama = time(2, 0)    # 02:00
yemek_saati3_bitis = time(3, 0)      # 03:00

# Zaman farkını hesapla
zaman_farki = tarih2 - tarih1

# Mesai ve yemek saatlerini toplam zamandan çıkar
def cikar_zaman(aralik_baslama, aralik_bitis, tarih1, tarih2):
    baslama = max(tarih1, datetime.combine(tarih1.date(), aralik_baslama))
    bitis = min(tarih2, datetime.combine(tarih2.date(), aralik_bitis))
    if bitis > baslama:
        return bitis - baslama
    return timedelta()

toplam_cikarilan_zaman = timedelta()
gecici_tarih = tarih1

while gecici_tarih < tarih2:
    if gecici_tarih.weekday() < 5:  # Hafta içi (Pazartesi'den Cuma'ya)
        toplam_cikarilan_zaman += cikar_zaman(mesai_baslama, mesai_bitis, gecici_tarih, tarih2)
        toplam_cikarilan_zaman += cikar_zaman(yemek_saati1_baslama, yemek_saati1_bitis, gecici_tarih, tarih2)
        toplam_cikarilan_zaman += cikar_zaman(yemek_saati2_baslama, yemek_saati2_bitis, gecici_tarih, tarih2)
        toplam_cikarilan_zaman += cikar_zaman(yemek_saati3_baslama, yemek_saati3_bitis, gecici_tarih, tarih2)
    gecici_tarih += timedelta(days=1)

# Toplam zaman farkından çıkar
geri_kalan_zaman = zaman_farki - toplam_cikarilan_zaman

# Kalan zamanı gün, saat ve dakika olarak hesapla
gunler = geri_kalan_zaman.days
saniye = geri_kalan_zaman.seconds
saat = saniye // 3600
dakika = (saniye % 3600) // 60

print(f"Toplam {gunler} gün, {saat} saat, {dakika} dakika geçmiştir ")
#2023-08-19 23:00