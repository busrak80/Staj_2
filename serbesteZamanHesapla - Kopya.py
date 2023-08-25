# Giriş saatini alayım
# Çıkış saatini alayım
# Tarih'tende içeride kaç gün geçirdiğini alayım
# Hafta içiyse 08:00 ve 17:30 arasını yoksay yemek saatlerini çıkart serbest zamana ekle
# Hafta içi değilse yemek saatlerini çıkart serbest zamana ekle
# Serbest zamanın toplamı > 2 saatse serbest zaman = serbest zaman
# Serbest zamanın toplamı > 2 değilse sebest zaman = 0


# 1 Çalışma saatlerini tanımlamam lazım
# 2 yemek saatlerini tanımlicam
# 30 dakika olarak baz alıcam
# calismaSaatleri = {8:00,.... 17:30}
# yemekSaatleri = {12:00, 12:30, 13:00}
#                {18:30, 19:00, 19:30}
#                {02:00, 02:30, 03:00}

import datetime

# girisTarihi_str = input("Giriş Tarihi Giriniz(Yıl-Ay-Gün örn: 2023-12-15 ) :")
# cikisTarihi_str = input("Çıkış Tarihi Giriniz(Yıl-Ay-Gün örn: 2023-12-15 ) :")
girisTarihi_str = "2023-08-08"
cikisTarihi_str = "2023-08-09"

# girisSaat_str = input("Giriş Saatini Giriniz(Saat:Dakika örn: 08:00 ) :")
# cikisSaat_str = input("Giriş Saatini Giriniz(Saat:Dakika örn: 17:30 ) :")
girisSaat_str = "08:00"
cikisSaat_str = "17:30"

calisanGirisSaati_time = datetime.datetime.strptime(girisSaat_str, "%H:%M")
calisanCikisSaati_time= datetime.datetime.strptime(cikisSaat_str, "%H:%M")

toplamSerbestSaat_minute = 0
giristekiSerbestZaman_minute = 0
cikistakiSerbestZaman_minute = 0

mesaiGirisSaati_str = "08:00"
mesaiCikisSaati_str = "17:30"

mesaiGirisSaati_datetime = datetime.datetime.strptime(mesaiGirisSaati_str, "%H:%M")
mesaiCikisSaati_datetime = datetime.datetime.strptime(mesaiCikisSaati_str, "%H:%M")


mesaiCikisSaati_time = datetime.time(hour=17, minute=30, second=0)
mesaiGirisSaati_time = datetime.time(hour=8, minute=0, second=0)

girisTarihi_datetime = datetime.datetime.strptime(girisTarihi_str, "%Y-%m-%d")
cikisTarihi_datetime = datetime.datetime.strptime(cikisTarihi_str, "%Y-%m-%d")

girisSaat_datetime = datetime.datetime.strptime(girisSaat_str, "%H:%M")
cikisSaat_datetime = datetime.datetime.strptime(cikisSaat_str, "%H:%M")

icerideGecirilenGun = (cikisTarihi_datetime - girisTarihi_datetime).days


def isWeekDay(girisTarihi_datetime):
    if girisTarihi_datetime.weekday() < 5:
        return True


def KesikliSerbestZamanHesapla(
    toplamSerbestSaat_minute, giristekiSerbestZaman_minute, gun
):
    if girisSaat_datetime < mesaiGirisSaati_datetime:
        giristekiSerbestZaman_datetime = mesaiGirisSaati_datetime - girisSaat_datetime
        giristekiSerbestZaman_minute = int(giristekiSerbestZaman_datetime.seconds / 60)
    else:
        giristekiSerbestZaman_datetime = datetime.time(hour=0, minute=0, second=0)

    if gun < 1:
        if cikisSaat_datetime > mesaiCikisSaati_datetime:
            cikistakiSerbestZaman_datetime = cikisSaat_datetime - mesaiCikisSaati_time
        else:
            cikistakiSerbestZaman_datetime = datetime.time(hour=0, minute=0, second=0)
    else:
        #!!!
        dummy_date = datetime.datetime(2000, 1, 1)
        datetime1 = datetime.datetime.combine(
            dummy_date, datetime.time(hour=23, minute=59, second=59)
        )
        datetime2 = datetime.datetime.combine(dummy_date, mesaiCikisSaati_time)

        cikisSaati_time = datetime.datetime.strptime(cikisSaat_str, "%H:%M")
        cikistakiSerbestZaman_datetime = datetime1 - datetime2

        cikistakiSerbestZaman_minutex = cikistakiSerbestZaman_datetime.seconds / 60
        cikistakiSerbestZaman_minutex += mesaiCikisSaati_time.second

    # giriş ve çıkışı dakikaya çevirdim
    if giristekiSerbestZaman_datetime.second > 60:
        giristekiSerbestZaman_minute = giristekiSerbestZaman_datetime.seconds / 60
    #datetime.timedelta nesnesinin dakika özelliği yok    
    if type(cikistakiSerbestZaman_datetime) == datetime:
        cikistakiSerbestZaman_minute = cikistakiSerbestZaman_datetime.second / 60
    elif type(cikistakiSerbestZaman_datetime) == datetime.time:
        cikistakiSerbestZaman_minute = cikistakiSerbestZaman_datetime.second / 60
    else:
        cikistakiSerbestZaman_minute = cikistakiSerbestZaman_datetime.seconds / 60


    if giristekiSerbestZaman_minute + cikistakiSerbestZaman_minute >= 120:
        # dakika cinsinden şu ana kadar bulduğum toplam serbest zamanı aldım
        giristekiSerbestZaman_min = giristekiSerbestZaman_datetime.second / 60
        cikistakiSerbestZaman_min = cikistakiSerbestZaman_datetime.seconds / 60
        toplamSerbestSaat_minute = (
            giristekiSerbestZaman_minute + cikistakiSerbestZaman_minute
        )
        return toplamSerbestSaat_minute


def FullSerbestZaman(gun, girisTarihi_datetime, toplamSerbestSaat_minute):
    if gun > 0:
        # gece 12 den itibaren çalışıyorum
        # gece 12'de gelmişim gibi sanallaştırıcam (göstericem)
        birSonrakiGunCalismayaBaslamaZamani_datetime = girisTarihi_datetime

        cikisSaatMevcutTarihicinGuncellenmis_datetime = cikisSaat_datetime.replace(
            year=girisTarihi_datetime.year,
            month=girisTarihi_datetime.month,
            day=girisTarihi_datetime.day,
        )

        birSonrakiGunSerbestZamanCalismaSaati_datetime = (
            cikisSaatMevcutTarihicinGuncellenmis_datetime
            - birSonrakiGunCalismayaBaslamaZamani_datetime
        )

        birSonrakiGunSerbestZamanCalismaSaati_minute = int(
            birSonrakiGunSerbestZamanCalismaSaati_datetime.seconds / 60
        )

        toplamSerbestSaat_minute += birSonrakiGunSerbestZamanCalismaSaati_minute
        return toplamSerbestSaat_minute

    else:
        # kendi giriş yaptığı saatten itibaren çalışıyor
        haftaSonuSerbestCalismaZamani_datetime = cikisSaat_datetime - girisSaat_datetime

        haftaSonuSerbestCalismaZamani_minute = (
            haftaSonuSerbestCalismaZamani_datetime.hour * 60
            + haftaSonuSerbestCalismaZamani_datetime.minute
        )

        if haftaSonuSerbestCalismaZamani_minute >= 120:
            toplamSerbestSaat_minute
            return toplamSerbestSaat_minute


if icerideGecirilenGun > 0:
    # içeride kalınan gün kadar gezinmek
    for gun in range(icerideGecirilenGun + 1):
        haftaiciMi = isWeekDay(girisTarihi_datetime)

        # hafta içiyse
        if haftaiciMi:
            toplamSerbestSaat_minute = KesikliSerbestZamanHesapla(
                toplamSerbestSaat_minute, giristekiSerbestZaman_minute, gun
            )

        # hafta sonuysa
        else:
            toplamSerbestSaat_minute = FullSerbestZaman(
                gun, girisTarihi_datetime, toplamSerbestSaat_minute
            )

        birGun = datetime.timedelta(days=1, hours=0, minutes=0, seconds=0)
        girisTarihi_datetime += birGun
else:
    haftaiciMi = isWeekDay(girisTarihi_datetime)

    # hafta içiyse
    if haftaiciMi:
        toplamSerbestSaat_minute = KesikliSerbestZamanHesapla(
            toplamSerbestSaat_minute, giristekiSerbestZaman_minute
        )

    # hafta sonuysa
    else:
        toplamSerbestSaat_minute = FullSerbestZaman(
            gun, girisTarihi_datetime, toplamSerbestSaat_minute
        )
toplamSerbestSaat_hour = int(toplamSerbestSaat_minute / 60)
print("Tebrikler {} saat serbest zaman kazandın".format(toplamSerbestSaat_hour))
