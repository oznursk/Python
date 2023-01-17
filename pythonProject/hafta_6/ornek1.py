"""
1-veri isimli klasör dosyası oluşturun
2-zip dosyasını veri klasörüne çıkartın
3-zip dosyasını içindeki csv dosyalarının tüm içeriğini tek bir csv dosyasında birleştirin
4-bu kayıtların tamamını sqlite veritabanına bir tablo oluşturarak yükleyin
5-kullanıcının belirlediği paaritenin
  kullanıcının belirlediği aralığın
  kullanıcın belirlediği degerin
  grafiğini çizdirin(veriler sqlitettan çekilecek)
"""
import os
import sqlite3
import zipfile
import pandas as pd

if not os.path.exists("veri"):
     os.mkdir("veri")

     arsiv=zipfile.ZipFile("pariteler_cikti_1hour_2022_2022.zip")
     arsiv.extractall("veri/")


     tum_dosyalar=os.listdir("veri")
     pandas_csvlistesi=[]
       for csv_dosya in tum_dosyalar:
         veri=pd.read_csv("veri/"+csv_dosya)
         del veri["volume"]
         pandas_csvlistesi.append(veri)

        birlesmis_csv_ler=pd.concat(pandas_csvlistesi)
        birlesmis_csv_ler.to_csv("hepsi.csv",index=False)

bag=sqlite3.connect("kripto.vt")
cursor=bag.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS parite(")
kayitlar=pd.read_csv("hepsi.csv")