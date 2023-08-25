import datetime

# Kullanıcıdan giriş tarihini ve saati alın
girisTarihi_str = input("Giriş Tarihi Giriniz (Yıl-Ay-Gün örn: 2023-12-15): ")
girisSaat_str = input("Giriş Saatini Giriniz (Saat:Dakika örn: 08:00): ")

# Kullanıcıdan çıkış tarihini ve saati alın
cikisTarihi_str = input("Çıkış Tarihi Giriniz (Yıl-Ay-Gün örn: 2023-12-15): ")
cikisSaat_str = input("Çıkış Saatini Giriniz (Saat:Dakika örn: 17:30): ")

# Tarih ve saatleri datetime nesnelerine çevirin
girisTarihi_datetime = datetime.datetime.strptime(girisTarihi_str, "%Y-%m-%d")
girisSaat_datetime = datetime.datetime.strptime(girisSaat_str, "%H:%M")

cikisTarihi_datetime = datetime.datetime.strptime(cikisTarihi_str, "%Y-%m-%d")
cikisSaat_datetime = datetime.datetime.strptime(cikisSaat_str, "%H:%M")

calismaSaatleri = [
    datetime.time(8, 0), datetime.time(8, 30), datetime.time(9, 0), datetime.time(9, 30),
    datetime.time(10, 0), datetime.time(10, 30), datetime.time(11, 0), datetime.time(11, 30),
    datetime.time(13, 0), datetime.time(13, 30), datetime.time(14, 0), datetime.time(14, 30),
    datetime.time(15, 0), datetime.time(15, 30), datetime.time(16, 0), datetime.time(16, 30),
    datetime.time(17, 0), datetime.time(17, 30)
]

yemekSaatleri = [
    datetime.time(12, 0), datetime.time(12, 30), datetime.time(13, 0),
    datetime.time(18, 30), datetime.time(19, 0), datetime.time(19, 30),
    datetime.time(2, 0), datetime.time(2, 30), datetime.time(3, 0)
]

def calculate_free_time(giris_datetime, cikis_datetime, calisma_saati, yemek_saati):
    toplam_serbest_dakika = 0
    current_datetime = giris_datetime

    while current_datetime < cikis_datetime:
        current_time = current_datetime.time()

        if current_time in calisma_saati and current_time not in yemek_saati:
            toplam_serbest_dakika += 30

        current_datetime += datetime.timedelta(minutes=30)

    return toplam_serbest_dakika

serbest_dakika = calculate_free_time(girisTarihi_datetime, cikisTarihi_datetime, calismaSaatleri, yemekSaatleri)

if serbest_dakika >= 120:
    serbest_dakika -= 120
else:
    serbest_dakika = 0

serbest_saat = serbest_dakika // 60
serbest_dakika %= 60

print("Tebrikler, {} saat {} dakika serbest zaman kazandınız.".format(serbest_saat, serbest_dakika))
