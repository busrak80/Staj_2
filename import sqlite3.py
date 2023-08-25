import sqlite3

# Veritabanına bağlanma
connection = sqlite3.connect("serbest_zaman.db")
cursor = connection.cursor()

# Kayıtları seçme
cursor.execute("SELECT * FROM giris_cikis")
veriler = cursor.fetchall()

# Kayıtları ekrana yazdırma
for veri in veriler:
    print(veri)

# Veritabanı bağlantısını kapatma
connection.close()
