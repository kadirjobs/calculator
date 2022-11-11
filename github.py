
#hesap makinası

from math import log
from math import sin
from math import cos

print("karekok icin=k,log icin log ,faktoriyel icin !,sin icin =sin,cos icin=cos toplama için= +,cıkarma için= -,çarpma için= *,bolme için /,üs almak için= **,mod için= % yaziniz")
faktoriyel=1
print("islem giriniz")
islem=input()

sayi1=int(input("birinci sayiyi giriniz:"))

if ((islem not in "k") and  (islem not in "!") and (islem not in "sin")  and (islem not in "cos")):

    sayi2=int(input("ikinci sayiyi giriniz:"))


if islem=="!":

     if sayi1 < 0:
        print("Negatif sayilarin faktoriyeli hesaplanamaz.")
     elif sayi1 == 0:
        print("0! = 1")
     else:
        for i in range(1,sayi1 + 1):
         faktoriyel= faktoriyel*i
         print(faktoriyel)
elif islem=="cos":
    sonuc=cos(sayi1)
    print(sonuc)
elif islem=="sin":
    sonuc=sin(sayi1)
    print(sonuc)
elif islem=="+":
    sonuc=sayi1+sayi2
    print(sonuc)
elif islem=="-":
     sonuc= sayi1-sayi2
     print(sonuc)
elif islem=="*":
     sonuc=sayi1*sayi2
     print(sonuc)
elif islem=="**":
    sonuc=sayi1**sayi2
    print(sonuc)
elif islem=="/" and sayi2!=0:
    sonuc=sayi1/sayi2
    print(sonuc)
elif islem=="%":
    sonuc=sayi1%sayi2
    print(sonuc)
elif islem=="k":
    sonuc=sayi1**0.5
    print(sonuc)

elif islem=="log":
    sonuc=log(sayi1,sayi2)
    print(sonuc)


else:
    print("gecersiz islem girdiniz..!")
