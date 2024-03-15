###############################################
# KOŞULLAR (CONDITIONS)
###############################################

# True-False'u hatırlayalım.
1 == 1
1 == 2

# if
if 1 == 1:
    print("something")

if 1 == 2:
    print("something")

number = 11

if number == 10:
    print("number is 10")

number = 10
number = 20

#kendini tekrar etme!! Fonksiyon yaz

def number_check(number):
    if number == 10:
        print("number is 10")

number_check(10)

#######################
# else
#######################

def number_check(number):
    if number == 10:
        print("number is 10")

number_check(12)
#12 sağlanmaz else kullanımı gerektirir.


def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(12)
#else blogu çalıştı

#######################
# elif
#birden fazla durumda
#######################

def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else: #10 a eşit ise
        print("equal to 10")

number_check(6)
number_check(10)

###############################################
# DÖNGÜLER (LOOPS)
###############################################
# for loop

#liste
students = ["John", "Mark", "Venessa", "Mariam"]

students[0]
students[1]
students[2]

#student nesnesi ile students listesinde gez
for student in students:
    print(student)
# sırayla listedeki elemanları yazdırır

for student in students:
    print(student.upper())
#her elemanın isimlerim tüm harflerini büyüterek yazdırır

#maaşları ifade eden bir liste
salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)


for salary in salaries:
    print(int(salary*20/100 + salary)) #yüzde 20 zam

for salary in salaries:
    print(int(salary*30/100 + salary))

for salary in salaries:
    print(int(salary*50/100 + salary))

def new_salary(salary, rate):
    return int(salary*rate/100 + salary)
#maaşı ve zamı girerek yeni maaşı hesaplayan fonk

new_salary(1500, 10)
new_salary(2000, 20)

#tüm maaşlara fonk çağırarak zam yapmak
for salary in salaries:
    print(new_salary(salary, 20))


salaries2 = [10700, 25000, 30400, 40300, 50200]

for salary in salaries2:
    print(new_salary(salary, 15))

#masslarının oranına göre farklı zam yap
for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))



#######################
# Uygulama - Mülakat Sorusu
#######################

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"
# çift indeksteki harfleri büyült tek indekstekileri küçült

range(len("miuul")) #0 dan lene kadar sayı üret
range(0, 5) #üstteki ile aynı

for i in range(len("miuul")):
    print(i)

# 4 % 2 == 0
# m = "miuul"
# m[0]

def alternating(string):
    new_string = ""
    # girilen string'in index'lerinde gez.
    #range o dan len boyutuna kadar sayı üretir
    for string_index in range(len(string)):
        # index çift ise büyük harfe çevir.
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        # index tek ise küçük harfe çevir.
        else:
            new_string += string[string_index].lower()
    print(new_string)

alternating("miuul")
alternating("yağmur yaşarbaş")

#######################
# break & continue & while
#######################

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary == 3000:
        break
    #koşul sağlandığında döngü durur ve çıkış yapar
    print(salary)


for salary in salaries:
    if salary == 3000:
        continue
    #sağlanan koşul atlanır ve dongü sonraki adımdan devam eder
    print(salary)


# while

number = 1
while number < 5:
    print(number)
    number += 1

#######################
# Enumerate: Otomatik Counter/Indexer ile for loop
#######################

students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, student)

for index, student in enumerate(students,1):
    print(index, student)
    #indexleri birden başlattık

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)
A
B

#######################
# Uygulama - Mülakat Sorusu
#######################
# divide_students fonksiyonu yazınız.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Venessa", "Mariam"]


def divide_students(students):
    groups = [[], []]#listenin içinde iki ayrı liste
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups

st = divide_students(students)
st[0]
st[1]


#######################
# alternating fonksiyonunun enumerate ile yazılması
#######################
#enumarte stingde hem kendisini hem indexi verir
def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating_with_enumerate("hi my name is john and i am learning python")

#######################
# Zip
#3 farklı listenin elemanlarını eişelemek ve bir arada deüerlendirmek
#######################

students = ["John", "Mark", "Venessa", "Mariam"]

departments = ["mathematics", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]
#aynı indexleri tupple formda eşleyerek bir listede tuttu
list(zip(students, departments, ages))

###############################################
# lambda, map, filter, reduce
###############################################

def summer(a, b):
    return a + b

summer(1, 3) * 9

new_sum = lambda a, b: a + b
#lambda kullan at fonklardır
#değişkenler bölümünde yer tutmaması gerekir
new_sum(4, 5)

# map
salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

new_salary(5000)

for salary in salaries:
    print(new_salary(salary))

#döngü yazmadan ilk fonksiyonu ikinci olan listeye uygular
list(map(new_salary, salaries))


# del new_sum
#fonk lambda ile tanımlamadan kullandık
#map ile tüm listeye uyguladık
list(map(lambda x: x * 20 / 100 + x, salaries))
list(map(lambda x: x ** 2 , salaries))

# FILTER
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))

# REDUCE
from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store)
#tüm elemanları topladı

#quiz sorusu
wages=[700,800,900,1000]
[wage*1.1 if wage>950 else wage*1.2 for wage in wages]

#quiz sorusu2
string="abracadabra"
group=[]

for index,letter in enumerate(string,1):
    if index*2%2==0:
        group.append(letter)

print(group)

#[yeni_değer if koşul else eski_değer for eleman in liste]


