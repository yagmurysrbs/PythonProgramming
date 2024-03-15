#1-
""" ListComprehension yapısıkullanarakcar
_crashesverisindekinumeric değişkenlerinisimlerinibüyükharfeçevirinizvebaşınaNUM
ekleyiniz.
"""

import seaborn as sns
df=sns.load_dataset("car_crashes")
df.columns

["NUM"+col.upper() for col in df.columns]


#2
""" ListComprehension yapısı kullanarakcar_crashesverisindeisminde"no" barındırmayan
değişkenlerin isimlerinin sonuna"FLAG" yazınız.
"""
import seaborn as sns
df=sns.load_dataset("car_crashes")
df.columns
#[col.upper() if "no" in col else col.upper() + "FLAG" for col in df.columns]
[col.upper() if "no" in col else col.upper() + "FLAG" for col in df.columns]

#3
"""ListComprehension yapısı
kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin
isimlerini seçiniz ve yeni 
bir data frame oluşturunuz"""

ogg_list=["abbrev","no_previous"]
# Yeni bir liste comprehension kullanarak farklı olan değişken adlarını seçme
new_cols = [col for col in df.columns if col not in ogg_list]

# Yeni DataFrame'i oluşturma
new_df = df[new_cols].copy()
new_df
