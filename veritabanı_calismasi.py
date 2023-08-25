from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
import mysql.connector
#import panel as pn
import tkinter as tk
from tkcalendar import Calendar



config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'port': 3306,  # Default MySQL port
    'database': 'serbest_zaman',
}


def deneme():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    insert_query = "INSERT INTO tarihsaat (giris_saat, cikis_saat, personel_id) VALUES (%s, %s, %s)"    

    veri1 = ""
    veri2 = ""
    veri3 = ""

    if hafta_ici_var.get() == 1:
        
        veri1 = giris_saat_entry.get()
        veri2 = cikis_saat_entry.get()
        veri3 = 1
    elif hafta_sonu_var.get() == 1:
        
        veri1 = haftasonu_giris_saat_entry.get()
        veri2 = haftasonu_cikis_saat_entry.get()
        veri3 = 1

   
    
    cursor.execute(insert_query, (veri1, veri2, veri3))
    connection.commit()

    cursor.close()
    connection.close()
    hesaplama_yap()  # Eklenen veri sonrası hesaplama işlemini çağır

def hesaplama_yap():
    calisma_baslangic = datetime.strptime("08:00", "%H:%M")
    calisma_bitis = datetime.strptime("17:30", "%H:%M")
    yemek_saatleri = [
        (datetime.strptime("12:00", "%H:%M"), datetime.strptime("13:00", "%H:%M")),
        (datetime.strptime("18:30", "%H:%M"), datetime.strptime("19:30", "%H:%M")),
        (datetime.strptime("02:00", "%H:%M"), datetime.strptime("03:00", "%H:%M"))
    ]

    hafta_ici = hafta_ici_var.get()
    hafta_sonu = hafta_sonu_var.get()

    toplam_serbest_zaman = timedelta()

    # Tarih ve saat bilgilerini kullanıcıdan alın
    giris_tarih = tarih_combobox.get()  # Kullanıcıdan giriş tarihini alın
    giris_saat = datetime.strptime(giris_saat_entry.get(), "%H:%M")

    cikis_tarih = tarih_combobox.get()  # Kullanıcıdan çıkış tarihini alın
    cikis_saat = datetime.strptime(cikis_saat_entry.get(), "%H:%M")

    # Kullanıcının giriş ve çıkış tarihleri arasındaki gün sayısını hesaplayın
    gun_sayisi = (cikis_tarih - giris_tarih).days + 1

    for gun in range(gun_sayisi):
        tarih = giris_tarih + timedelta(days=gun)
        tarih = tarih.replace(hour=0, minute=0, second=0, microsecond=0)

        if tarih.weekday() < 5 and hafta_ici:  # Hafta içi ise hesapla
            serbest_zaman_haftaici = serbest_zaman_hesapla_haftaici(calisma_baslangic, calisma_bitis, yemek_saatleri, giris_saat, cikis_saat)
            toplam_serbest_zaman += serbest_zaman_haftaici

        if tarih.weekday() >= 5 and hafta_sonu:  # Hafta sonu ise hesapla
            serbest_zaman_haftasonu = serbest_zaman_hesapla_haftasonu(yemek_saatleri, giris_saat, cikis_saat)
            toplam_serbest_zaman += serbest_zaman_haftasonu

    serbest_zaman_label.config(text="Toplam serbest zamanınız: {}".format(toplam_serbest_zaman))


def serbest_zaman_hesapla_haftaici(calisma_baslangic, calisma_bitis, yemek_saatleri, giris_saat, cikis_saat):
    serbest_zaman = timedelta()
    #Eğer giris_saat çalışma başlangıç saatinden önce ise, serbest zaman calisma_baslangic ile giris_saat arasındaki süre olacaktır.
    if giris_saat < calisma_baslangic:
        serbest_zaman += calisma_baslangic - giris_saat
    #Eğer cikis_saat çalışma bitiş saatinden sonra ise, serbest zaman cikis_saat ile calisma_bitis arasındaki süre olacaktır.
    if cikis_saat > calisma_bitis:
        serbest_zaman += cikis_saat - calisma_bitis
    #Her bir yemek aralığı için, eğer yemek aralığının başlangıç saati calisma_baslangic ve bitiş saati calisma_bitis aralığında ise, o yemek aralığının süresi serbest zamandan çıkarılır.
    for yemek_araligi in yemek_saatleri:
        if yemek_araligi[0] >= calisma_baslangic and yemek_araligi[1] <= calisma_bitis:
            serbest_zaman -= yemek_araligi[1] - yemek_araligi[0]

    return serbest_zaman

def serbest_zaman_hesapla_haftasonu(yemek_saatleri, giris_saat, cikis_saat):
    serbest_zaman = timedelta()

    if giris_saat < cikis_saat:
        serbest_zaman += cikis_saat - giris_saat

    for yemek_araligi in yemek_saatleri:
        serbest_zaman -= yemek_araligi[1] - yemek_araligi[0]

    return serbest_zaman
    


# Ana pencere oluşturma
root = Tk()
root.title(" Serbest Zaman Hesaplama")
root.geometry("400x400")

# Hafta içi seçeneği
hafta_ici_var = BooleanVar()
hafta_ici_var.set(True)
hafta_ici_check = Checkbutton(root, text="Hafta İçi", variable=hafta_ici_var)
hafta_ici_check.pack()

# Hafta içi saat girişleri
giris_saat_label = Label(root, text="Giriş Saati (HH:MM):")
giris_saat_label.pack()
giris_saat_entry = Entry(root)
giris_saat_entry.pack()

cikis_saat_label = Label(root, text="Çıkış Saati (HH:MM):")
cikis_saat_label.pack()
cikis_saat_entry = Entry(root)
cikis_saat_entry.pack()

# Hafta sonu seçeneği
hafta_sonu_var = BooleanVar()
hafta_sonu_var.set(False)
hafta_sonu_check = Checkbutton(root, text="Hafta Sonu", variable=hafta_sonu_var)
hafta_sonu_check.pack()

# Hafta sonu saat girişleri
haftasonu_giris_saat_label = Label(root, text="Giriş Saati (HH:MM):")
haftasonu_giris_saat_label.pack()
haftasonu_giris_saat_entry = Entry(root)
haftasonu_giris_saat_entry.pack()

haftasonu_cikis_saat_label = Label(root, text="Çıkış Saati (HH:MM):")
haftasonu_cikis_saat_label.pack()
haftasonu_cikis_saat_entry = Entry(root)
haftasonu_cikis_saat_entry.pack()

# Hesaplama butonu
hesaplama_button = Button(root, text="Hesapla", command=deneme)
hesaplama_button.pack()

# Serbest zaman sonucu
serbest_zaman_label = Label(root, text="")
serbest_zaman_label.pack()

# Arayüzü çalıştırma
root.mainloop()
