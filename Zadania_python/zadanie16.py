a=float(input())
b=float(input())
c=float(input())

#def oznacza funkcje

#maksimum z dwoch liczb
def maksimum (a,b):
    if a>b:
        return a
    elif b>a:
        return b

#minimum z trzech liczb
def minimum (a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    elif c<a and b<c:
        return c
    elif a==b==c:
        print(f"liczby {a,b,c} sa rowne")

#liczba nieparzysta
def nieparzysta(a):
    if a%2==0:
        return "parzysta"
    else:
        return "nieparzysta"

#wartosc bezwgledna
def bezwgledna(a):
    if a>0:
        return a
    else :
        return -a

#suma wielu wartosci
def suma_wartosci(a,b,c): suma=0



print(maksimum(a,b))
print(minimum(a,b,c))
print(nieparzysta(a))
print(bezwgledna(a))
print(suma_wartosci(a,b,c))
