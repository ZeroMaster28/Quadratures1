#! /usr/bin/python3.6

#Michał Sobieraj , WMS IV
#Analiza Numeryczna grupa 1/czwartkowa


import math


#liczymy kwadraturę trapezów od a=x0 do b=xn
def kwadratura(f,a,b,n):
    delta=(b-a)/n
    suma=0
    for i in range(1,n): suma+=f(a+delta*i)
    suma+=f(a)/2+f(b)/2
    return suma*delta;

#stala asymptotyczna zależna od funkcji (prawa strona równości)
def stala(df,a,b):
    return (b-a)*(b-a)*(df(a)-df(b))/12


def result(calka,f,df,a,b,l):
    I = calka(b) - calka(a)
    for n in l:

        #kwadratura na n węzłach i wspolczynnik cn który zbiega do cf
        Qn = kwadratura(f, a, b, n)
        diff=I-Qn
        cn=n*n*diff

        #stala z prawej strony równania
        cf=stala(df,a,b)

        #przy n zmierzajacym do niesk. fixQ zbiega do I
        fixQ = Qn + cf/(n*n)
        value= (n*n)*(I-fixQ)

        print((l.__len__()-math.ceil(math.log10(n)))*" ",n,"|",Qn,"|",cn,"|",fixQ,"|",value,"|",diff)
    return;


#ile linijek chcemy zobaczyć: wiecej niz 8 nie ma sensu
przypadki =7



#Ponieżej zamieściłem przykładowe funkcje do przetestowania:
#
# #f(x)=sinx , x in (0,Pi)
# calka= lambda x: (-1)*math.cos(x)
# funkcja=math.sin
# pochodna=math.cos
# a=0
# b=math.pi

#
# #f(x)=e^x , x in (0,1)
# calka=math.exp
# funkcja=math.exp
# pochodna=math.exp
# a=0
# b=1


# #f(x)=2x , x in (0,1)
# calka= lambda x: x*x
# funkcja= lambda x: 2*x
# pochodna= lambda x: 2
# a=0
# b=1




list= list()
for i in range(1,przypadki): list.append(pow(10,i))
print("stala asymptotyczna c(f)=",stala(pochodna,a,b))
print(przypadki*" ","n | Qn(f) | n^2*(I(f)-Qn(f)) | fixQ(f) | n^2*(I(f)-fixQ(f) | I(f)-Qn(f))")
result(calka,funkcja,pochodna,a,b,list)