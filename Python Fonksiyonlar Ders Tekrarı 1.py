# def bir_fonksiyonadi():
    #Fonksiyonun çalıştıracağı satırlar
# bir_fonsiyonadi()
# 1-Basit Fonksiyon
def merhabade():
    print("Merhaba")
    print("Nasılsın")
# 2-Fonksiyon çağırma
a = 2
b = 3
def merhabade():
    print("Merhaba")
    print("Nasılsın")
def topla():
    merhabade()
    print("Toplam: ",a+b)
merhabade()
merhabade()
topla()
# Diğer Örnek Basit Fonksiyon
def selamla():
    print("Selam")
    print("Merhaba")
    selamla()
    selamla()
    selamla()
# Diğer Örnek 2 Basit Fonksiyon
# topla fonksiyonu oluştur. klavyeden girilen iki sayıyı toplasın.
def topla():
  s1 = int( input("1.Sayıyı gir:") )
  s2 = int( input("2.Sayıyı gir:") )
  toplam = s1+s2
  print(f"{s1} ve {s2} toplamı: {toplam}")
topla()
# Diğer Örenk 3 Basit Fonksiyon
def kmerhabade():
  print("\033[31m Merhaba")
def ymerhabade():
  print("\033[32m Merhaba")
for tr in range(5):
  kmerhabade()
  ymerhabade()
def merhabade_k():
  print("\033[31m Merhaba")
def merhabade_y(): print("\033[32m Merhaba")
for tr in range(5):
  merhabade_k()
  merhabade_y()
def yaz():
  print ("merhaba")
  print ("nasılsın")
def kırmızıyaz():
  print ("\033[31m kırmızı \033[0m")
a=4
b=5
def topla():
  print("\033[32m Toplam: \033[36m",a+b,"\033[0m")
for i in range(5):
  yaz()
  kırmızıyaz()
  topla() 


