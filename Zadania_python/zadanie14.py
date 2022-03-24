import random #losowanie liczb

#listy
liczby=[]
twoje_liczby=[]
odgadniete_liczby=[]

for user in range(0,6):
liczba=(random.randint(1,50))
liczby.append(liczba) #dodawanie do listy

while True:
    print("Podaj 6 liczb od 1 do 50: \n")
    for user in range(0,6):
    a=input()
    twoje_liczby.append(int(a))
    print(f"Twoja lista liczb to {twoje_liczby}")
    break
