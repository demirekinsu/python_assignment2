#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Soru 1 – Sayı Analizi


# In[3]:


sayi = int(input("Bir sayı giriniz: "))
if sayi > 0  :
    if sayi % 2 == 0:
        print("Pozitif çift")
    else:
        print("Pozitif Tek")
elif sayi < 0 :
    if sayi % 2 == 0:
        print("Negatif Çift")
    else:
        print("Negatif Tek")
else:
    print("Sıfır")


# In[5]:


# Soru 2 – Harf Frekansı (String)


# In[7]:


kelime = input("Bir kelime giriniz: ")

frekans = {}

for harf in kelime:
    if harf in frekans:
        frekans[harf] += 1
    else:
        frekans[harf] = 1

print(frekans)


# In[9]:


# Soru 3 – Şifre Kontrolü (String Metotları)


# In[11]:


sifre = input("Şifrenizi giriniz: ")
uzunluk = len(sifre) >= 8
buyuk_harf = any(harf.isupper() for harf in sifre)
rakam = any(harf.isdigit() for harf in sifre)

if uzunluk and buyuk_harf and rakam:
    print("Şifre Geçerli")
else:
    print("Şifre Geçersiz.")
    if not uzunluk:
        print("- En az 8 karakter olmalı:")
    if not  buyuk_harf:
        print("- En az 1 büyük harf olmalı:")
    if not rakam:
        print("- En az 1 rakam olmalı")


# In[13]:


#Soru 4 – Liste İşlemleri


# In[15]:


liste = [12, 4, 9, 25, 30, 7, 18]
ortalama = sum(liste) / len(liste)
print(ortalama)

buyuk_sayilar = []
for l in liste:
    if l > ortalama :
        buyuk_sayilar.append(l)
print("Ortalamadan büyük sayılar: ", buyuk_sayilar)


# In[17]:


# Soru 5 – Nested Loop (Desen)


# In[19]:


for i in range(1, 6):
    print("*" * i)


# In[21]:


# Soru 6 – While Döngüsü


# In[23]:


toplam = 0
adet = 0

while True:
    sayi = int(input("Bir sayı girin (0 çıkış için): "))
    if sayi == 0:
        break
    toplam += sayi
    adet += 1
if adet > 0:
    ortalama = toplam / adet
    print("Girilen sayıların toplamı:", toplam)
    print("Girilen sayıların ortalaması:", ortalama)
else:
    print("Hiç sayı girilmedi.")


# In[25]:


# Soru 7 – Palindrom Kontrolü


# In[27]:


kelime = input("Bir kelime giriniz: ")

if kelime == kelime[::-1]:
    print(kelime, "Palindrom ")
else:
    print(kelime, "Palindrom Değil ")


# In[29]:


# Soru 8 - List Comprehension


# In[31]:


liste = [i**2 for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print("Hem 3'e hem 5'e bölünebilenlerin kareleri:", liste)


# In[33]:


# Soru 9 - String İşlemleri


# In[35]:


cumle = "python summer camp "
kelimeler = cumle.split()
yeni_kelimeler = [kelime.capitalize() for kelime in kelimeler]
yeni_cumle = " ".join(yeni_kelimeler)
print(yeni_cumle)


# In[37]:


# Mini Proje - Film Yorumu Analizi


# In[39]:


yorumlar = [
    "Filime aşık oldum",
    "Hiç beğenmedim",
    "İdare ederdi",
    "Çok akıcıydı film ",
    "Daha iyi olabilirdi"
]

print("Toplam yorum sayısı:", len(yorumlar))
iyi_sayisi = sum("iyi" in y.lower() for y in yorumlar)
print('"iyi" geçen yorum sayısı:', iyi_sayisi)
en_uzun = max(yorumlar, key=len)
en_kisa = min(yorumlar, key=len)
print("En uzun yorum:", en_uzun)
print("En kısa yorum:", en_kisa)
uzunluklar = [len(y) for y in yorumlar]
print("Ortalama uzunluk:", sum(uzunluklar)/len(uzunluklar), "karakter")

