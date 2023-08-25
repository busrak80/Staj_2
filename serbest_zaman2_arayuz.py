from tkinter import *
from tkinter import messagebox
from datetime import datetime, timedelta, time

def calculate_time_difference():
    tarih1_str = tarih1_entry.get()
    tarih2_str = tarih2_entry.get()

    try:
        tarih1 = datetime.strptime(tarih1_str, '%Y-%m-%d %H:%M')
        tarih2 = datetime.strptime(tarih2_str, '%Y-%m-%d %H:%M')

        mesai_baslama = time(8, 0)
        mesai_bitis = time(17, 30)
        yemek_saati1_baslama = time(12, 0)
        yemek_saati1_bitis = time(13, 0)
        yemek_saati2_baslama = time(18, 30)
        yemek_saati2_bitis = time(19, 30)
        yemek_saati3_baslama = time(2, 0)
        yemek_saati3_bitis = time(3, 0)

        zaman_farki = tarih2 - tarih1

        def cikar_zaman(aralik_baslama, aralik_bitis, tarih1, tarih2):
            baslama = max(tarih1, datetime.combine(tarih1.date(), aralik_baslama))
            bitis = min(tarih2, datetime.combine(tarih2.date(), aralik_bitis))
            if bitis > baslama:
                return bitis - baslama
            return timedelta()

        toplam_cikarilan_zaman = timedelta()
        gecici_tarih = tarih1

        while gecici_tarih < tarih2:
            if gecici_tarih.weekday() < 5:
                toplam_cikarilan_zaman += cikar_zaman(mesai_baslama, mesai_bitis, gecici_tarih, tarih2)
                toplam_cikarilan_zaman += cikar_zaman(yemek_saati1_baslama, yemek_saati1_bitis, gecici_tarih, tarih2)
                toplam_cikarilan_zaman += cikar_zaman(yemek_saati2_baslama, yemek_saati2_bitis, gecici_tarih, tarih2)
                toplam_cikarilan_zaman += cikar_zaman(yemek_saati3_baslama, yemek_saati3_bitis, gecici_tarih, tarih2)
            gecici_tarih += timedelta(days=1)

        geri_kalan_zaman = zaman_farki - toplam_cikarilan_zaman

        gunler = geri_kalan_zaman.days
        saniye = geri_kalan_zaman.seconds
        saat = saniye // 3600
        dakika = (saniye % 3600) // 60

        result_label.config(text=f"Toplam {gunler} gün, {saat} saat, {dakika} dakika geçmiştir")

    except ValueError:
        messagebox.showerror("Hata", "Geçersiz tarih formatı!")

# Arayüz oluşturma
root = Tk()
root.title("Zaman Farkı Hesaplama")
root.geometry("400x300")

title_label = Label(root, text="Serbest Zaman  Hesaplama", font=("Helvetica", 16, "bold"))
title_label.pack(pady=20)

tarih1_label = Label(root, text="İlk Tarih (YYYY-MM-DD HH:MM):", font=("Helvetica", 12))
tarih1_label.pack()

tarih1_entry = Entry(root, font=("Helvetica", 12))
tarih1_entry.pack()

tarih2_label = Label(root, text="İkinci Tarih (YYYY-MM-DD HH:MM):", font=("Helvetica", 12))
tarih2_label.pack()

tarih2_entry = Entry(root, font=("Helvetica", 12))
tarih2_entry.pack()

calculate_button = Button(root, text="Hesapla", font=("Helvetica", 12), command=calculate_time_difference)
calculate_button.pack(pady=20)

result_label = Label(root, text="", font=("Helvetica", 16))
result_label.pack()

root.mainloop()