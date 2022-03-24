print("Kalkulator")
a=float(input("Podaj a: "))
b=float(input("Podaj b: "))
print("Co chcesz zrobic?")
print("Masz do wyboru: dodawanie, odejmowanie, mnozenie, dzielenie")
x=input()

if x==dodawanie: 
    print(suma=a+b)
elif x==odejmowanie:
    print(roznica=a-b)
elif x==mnozenie:
    print(iloczyn=a*b)
elif x==dzielenie:
    if b==0:
        print("NIE DZIEL PRZEZ 0!")
    else:
        print(iloraz=a/b)


