"""
1- veri isimli bir klosör oluşturun

2- zip dosyasını veri klosörüne çıkartın

3- zip dosyası içindeki tüm dosyaların içeriğini tek bir csv dosyasında birleştirin ama volume olmasın

4- bu kayıtların tamamını sqlite veritabanına bir tablo oluşturarak yükleyin

5- kullanıcının belirlediği paritenin
   kullanıcının belirlediği aralığın
   kullanıcının belirlediği değerin grafiğini çizdirin
"""
import os
import zipfile
import pandas as pd
import sqlite3

path = "5.ders/veri"
if not os.path.exists(path):
    os.mkdir(path)

    arsiv = zipfile.ZipFile("5.ders/pariteler_cikti_1hour_2022_2022.zip")
    arsiv.extractall(path + "/")

    allFiles = os.listdir(path)
    pandas_csv_listesi = []
    for csv_dosya in allFiles:
       veri = pd.read_csv(path+"/" + csv_dosya)
       del veri["volume"]
       pandas_csv_listesi.append(veri)
    
    birlesmis_csv_ler = pd.concat(pandas_csv_listesi)
    birlesmis_csv_ler.to_csv("5.ders/hepsi.csv", index=False)

bag = sqlite3.connect("kripto.nevfel")
cursor = bag.cursor()
cursor.execute("""
CREATE TABLE parite(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    otime DATETIME, open FLOAT,
    high FLOAT, low FLOAT, close FLOAT);
""")