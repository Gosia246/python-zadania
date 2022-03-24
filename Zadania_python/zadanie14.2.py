import random
wylosowane_liczby=random.randint(1,50)
strzaly=[]
trafione=[]


wylosowane_liczby.append(strzaly)
b=int(input(f"Podaj liczbe {i+1} z 6: "))
while b>50 or b<1:
    print("Podaj liczbe z zakresu od 1 do 50: ")
    b=int(input(f"Podaj liczbe {i+1} z 6: "))
    strzaly.append(b)

print(*losowanie, sep=', ')
print("Twoje liczby: ")
print(*strzaly, sep=', ')

trafione=set(losowanie)&set(strzaly)

if len(trafione)>0:
    print(f"Trafiles {len(trafione)} "
else :
    print("Nie trafiles zadnej liczby.")