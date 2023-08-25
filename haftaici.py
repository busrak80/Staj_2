from datetime import datetime, timedelta

def serbest_zaman_hesapla_haftaici(calisma_baslangic, calisma_bitis, yemek_saatleri):
    
    giris_saat = datetime.strptime(input("Giriş saatini girin (HH:MM): "), "%H:%M")
    cikis_saat = datetime.strptime(input("Çıkış saatini girin (HH:MM): "), "%H:%M")

    
    serbest_zaman = timedelta()

    if giris_saat < calisma_baslangic:
        serbest_zaman += calisma_baslangic - giris_saat

    if cikis_saat > calisma_bitis:
        serbest_zaman += cikis_saat - calisma_bitis

    # Yemek saatlerini serbest zamandan çıkar
    for yemek_araligi in yemek_saatleri:
        if yemek_araligi[0] >= calisma_baslangic and yemek_araligi[1] <= calisma_bitis:
            serbest_zaman -= yemek_araligi[1] - yemek_araligi[0]

    return serbest_zaman
# Çalışma saatlerini ve yemek saatlerini tanımla
calisma_baslangic = datetime.strptime("08:00", "%H:%M")
calisma_bitis = datetime.strptime("17:30", "%H:%M")
yemek_saatleri = [(datetime.strptime("12:00", "%H:%M"), datetime.strptime("13:00", "%H:%M")),
                  (datetime.strptime("18:30", "%H:%M"), datetime.strptime("19:30", "%H:%M")),
                  (datetime.strptime("02:00", "%H:%M"), datetime.strptime("03:00", "%H:%M"))]

serbest_zaman = serbest_zaman_hesapla_haftaici(calisma_baslangic, calisma_bitis, yemek_saatleri)

print("Şu anki serbest zamanınız:", serbest_zaman) 