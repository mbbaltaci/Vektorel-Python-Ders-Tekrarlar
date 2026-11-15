'''
# Varsayılan(Default) parametre değeri
def selamla(kim="---"):
    print("Selam",kim)
    print("Nasılsın")
    selamla()
    selamla("Emir")
def topla(aa,bb):
    print(aa,"ile",bb,"toplamı:",aa+bb)
def carp(a,b): print(a,"ile",b,"çarpımı:",a*b)
xx = 10; yy = 3
topla(20,6)
# topla(20) # bir parametre olduğu için hata verir
carp(xx,yy)
carp(xx,2)
# carp(xx) # bir parametre olduğu için hata verir
# default değeri olanlar sonda olmalı
# bu foksiyonda en az tc ve ad olmalı
def kayit_ekle(tc,adi,num="no yok",cins="--"):
    print(f"Kayıt ekleme işlemi:\n\
        TC       :{tc}\
        Adı      :{adi}\
        Numarası :{num}\
        kaydı başarıyla eklendi.")
kayit_ekle(56762132202,"Erhan ENSAR")
kayit_ekle(56762132202,"Esma CANTEZ",13,"K")
# enaz iki parametre zorunlu olduğundan hata verir.
# kayit_ekle(56762132202)
# kayit_ekle()
# Bu fonksiyonları çağırırken iki parametre göndermek gerek. Gönderilmese de kendisi atama yapabilir.
# default değerli parametreler sonda tanımlanır
def topla(aa=5,bb): # en az bir parametre gerek
    print(aa,"ile",bb,"toplamı:",aa+bb)

# Bu fonksiyonda parametre gönderilmese de hata vermez
def seriTopla(a=0,b=0,c=0):
    print("Toplam: ",a+b+c)

def carp(a,b=1): print(a,"x",b,"=",a*b)

xx = 10
yy = 3
topla(20,6)
topla(20)# bir parametre olsa da çalışır
seriTopla()
seriTopla(3)
seriTopla(3,4)
seriTopla(2,6,3)
# seriTopla(6,5,2,8) # 4 parametre olmaz
carp(xx,yy)
carp(xx,2)
carp(xx) # bir parametre olsa da çalışır
'''
# parametre default değeri
def topla(a=0,b=10): # a ve b değerleri fonksiyon çağırımında bir şey girilmez ise ne olacağı...
  toplam = a + b
  print(f"{a} ve {b} toplamı: {toplam}")
topla(7,2)
topla(7,21)
topla(7)
topla()
# parametre alan fonksiyon
def topla(a,b): # a ve b fonksiyon parametreleri
  toplam = a + b
  print(f"{a} ve {b} toplamı: {toplam}")

s1 = int( input("1.Sayıyı gir:") )
s2 = int( input("2.Sayıyı gir:") )
topla(s1,s2)
topla(7,2)

