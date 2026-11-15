# 2-Değer/parametre alan fonksiyonlar
def selamla(kim):
    print("Selam", kim)
    print("Nasılsın")
    selamla("Bartu")
    selamla("Emir")
    selamla()
def topla(aa,bb):
    print(f"{aa} ile {bb} toplamı:",aa+bb)
xx = 10
yy = 3
topla(20,6)
topla(xx,yy)
def kare_bul(sayi):
    print(f"{sayi} sayısının karesi {sayi**2} sayısıdır")
    kare_bul(9)
def kereYazdir(kelime,adet):
    print(kelime*adet)
    kereYazdir('Merhaba\n',10)
def topla(aa,bb):
    print(aa,"ile",bb,"toplamı:",aa+bb)
def carp(a,b): print(a,"ile",b,"çarpımı:",a*b)
def cikar(aa,bb): print(f"{aa} ile {bb} farkı:",aa-bb)
def bol(x,y): print(x,"ile",y,"bolumu:",x/y)

def tamBol(xx,yy):
    print(xx,"ile",yy,"küsuratsız bölümü:",xx//yy)
def ustAl(aa,bb): print(aa,"üzeri",bb,"=",aa**bb)
xx = 10
yy = 3
bol(xx,yy)
topla(20,6)
carp(xx,yy)
carp(xx,2)
tamBol(xx,yy)
ustAl(xx,yy)
def topla(a,b): # a ve b fonksiyon parametreleri
  toplam = a + b
  print(f"{a} ve {b} toplamı: {toplam}")
s1 = int( input("1.Sayıyı gir:") )
s2 = int( input("2.Sayıyı gir:") )
topla(s1,s2)
topla(7,2)
topla(7,21)
