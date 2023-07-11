# -*- coding: utf-8 -*-
"""
Kod   : Ahmet Aksoy
Sistem: Ubuntu 22.04 LTS
Python: Python 3.10.11
Modül : JPype1 1.4.1
Java  : zemberek-tum-2.0.jar
Tarih : 2023-07-08
"""
import jpype    # pip install jpype1

# JVM başlat
jpype.startJVM("/usr/lib/jvm/java-17-openjdk-amd64/lib/server/libjvm.so",
         "-Djava.class.path=/home/axax/dj_projects/derlemprj/zemberek-tum-2.0.jar", "-ea")
# Türkiye Türkçesine göre çözümlemek için gerekli sınıfı hazırla
Tr = jpype.JClass("net.zemberek.tr.yapi.TurkiyeTurkcesi")
# tr nesnesini oluştur
tr = Tr()
# Zemberek sınıfını yükle
Zemberek = jpype.JClass("net.zemberek.erisim.Zemberek")
# zemberek nesnesini oluştur
zemberek = Zemberek(tr)

# Ana dosyadaki kelimeleri yükle
def kelime_yukle(filename):
    kelimeler = []
    with open(filename,"r") as f:
        kelimeler = [k.strip() for k in f.readlines()]
    return kelimeler

def kelimeleri_cozumle(kelimeler, kaydet=False):
    say =0
    yok=0
    if kaydet:
        f1 = open("derlem/derlemtr.txt","w")
        f2 = open("hamveriler/denetimsiz.txt","w")

    for kelime in kelimeler:
        yanit = zemberek.kelimeCozumle(kelime)
        if (yanit):
            s = str(yanit[0])
            if len(s)>0:
                ss=s.split(':')
                kok="********"
                if len(ss)>=2:
                    kok = ss[2][:-4]
                    say += 1
                    print(say, kok, kelime)
                    if kaydet:
                        print(kelime,file=f1)
                else:
                    # kok boyutu 2 karakterden az
                    if kaydet:
                        print(kelime,file=f2)
            else:
                # geçersiz yanıt
                if kaydet:
                    print(kelime,file=f2)
        else:
            # yanıt yok -> kelime onaylanmıyor
            if kaydet:
                print(kelime,file=f2)

    if kaydet:
        f1.close()
        f2.close()


if __name__ == "__main__":

    kelimeler = kelime_yukle("hamveriler/tumkelimeler001.txt")
    print("Kelime sayısı= ", len(kelimeler))
    kelimeleri_cozumle(kelimeler, kaydet=True)

    jpype.shutdownJVM()
    jpype = None
