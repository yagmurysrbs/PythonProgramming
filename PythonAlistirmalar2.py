#5
""": Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
return eden fonksiyon yazınız."""

liste=[2,13,18,93,22]

def func(gelenliste):
    ciftliste=[]
    tekliste=[]
    for i in gelenliste:
        if i % 2 == 0:
            ciftliste.append(i)
        else:
            tekliste.append(i)
    return ciftliste,tekliste
#return döngünün dışına yaz!!!!!

ciftler,tekler=func(liste)
ciftler
tekler

#6
""" Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız."""

ogrenciler=["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for index, ogrenci in enumerate(ogrenciler, 1):
    if index <= 3:
        print(f"Mühendislik Fakültesi {index}. öğrenci: {ogrenci}")
    else:
        print(f"Tıp Fakültesi {index - 3}. öğrenci: {ogrenci}")

#7
"""Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
almaktadır. Zip kullanarak ders bilgilerini bastırınız."""

ders_kodu=["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi=[3,4,2,4]
kontenjan=[30,75,150,25]

ders_bilgileri = zip(ders_kodu, kredi, kontenjan)

# Her bir tuple'ı döngüyle gezerek bilgileri yazdırma
for ders in ders_bilgileri:
    ders_kodu, ders_kredi, ders_kontenjan = ders
    print(f"Kredisi {ders_kredi} olan {ders_kodu} dersinin kontenjanı {ders_kontenjan} kişidir.")

#8-
"""Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir."""

kume1=set(["data","python"])
kume2=set(["data","function","qcut","lambda","python","miuul"])

if kume1.issuperset(kume2):
    ortak=kume1.intersection(kume2)
    print(ortak)
else:
    fark=kume2.difference(kume1)
    #farkda genis kuneden kucuk kume cıkar
    print(fark)
#####################################################################3

