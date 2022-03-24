import random
wylosowana_liczba=random.randint(1,20)
liczby=[] #lista

while True: #petla while - dopoki cos sie dzieje
    liczba=input("Podaj liczbe calkowita od 1 do 20:")
    if int(liczba)==int(wylosowana_liczba):
        print("Brawo, odgadles liczbe!")
        print(f"Zgadles po {len(liczby)} po probach")
        break
    else :
        print("To nie ta liczba, probuj dalej")
        liczby.append(liczba) #dodawanie do listy
        print(liczby)
        continue
    #funkcja "len" zwraca liczbe prob

