#PYTHON ALIŞTIRMALAR
#1- VERİLEN DEĞERLERİN VERİ YAPILARINI İNCELEYİNİZ

x=8
type(x)

y=3.2
type(y)

z=8j+18
type(z)

a="hello world"
type(a)

b=True
type(b)

c=23<22
type(c)

l=[1,2,3,4]
type(l)

d={"Name":"Jake",
   "Age":27,
   "Adress":"Dowtown"}
type(d)
#dict

t=("Machine Learning","Data Science")
type(t)

s={"Python","Machine Learning","Data Science"}
type(s)
#set

#2-: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
#kelime kelime ayırınız.

text="The goal is to turn data into information, and information into insight."
yenitext=""
for x in text:
    if x=="," or x==".":
        yenitext+=""
    else:
        yenitext+=x.upper()
yenitext=yenitext.split()
yenitext

#string metodları replace,upper,split

#3-
"""Verilen listeye aşağıdaki adımları uygulayınız.
Adım 1: Verilen listenin eleman sayısına bakınız.
Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
Adım 4: Sekizinci indeksteki elemanı siliniz.
Adım 5: Yeni bir eleman ekleyiniz.
Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz."""

lst=["D","A","T","A","S","C","I","E","N","C","E"]
len(lst)
lst[0]
lst[10]
dataliste=lst[:4]
dataliste
lst.remove(lst[8])
#del list[8]
lst
lst.insert(8,"yeni")
#append sadece listenin sonuna ekler
#insert ile eklenecek konumu belirleriz
lst.insert(8,"N")
#update fonk sözlükleri günceller
#listelerde kullanılmaz

#4-
"""Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
Adım 1: Key değerlerine erişiniz.
Adım 2: Value'lara erişiniz.
Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
Adım 5: Antonio'yu dictionary'den siliniz"""

dict={"Chistian":["America",18],
      "Daisy":["England",12],
      "Antonio":["Spain",22],
      "Dante":["Italy",25]}

dict.values()
dict.keys()

dict["Daisy"][1] = 13
dict["Ahmet"] = ["Turkey", 24]
dict.update({"Ahu": ["Turkey", 23]})
del dict["Antonio"]
dict
