print("Gra papier, kamien, nozyce")

import random
strzal_komputera=["papier", "kamien", "nozyce"]
a=(random.choice(strzal_komputera))

wygrane=[]
przegrane=[]

if "wygrana":
    wygrane.append
elif "przegrana":
    przegrane.append

print("Wybierz papier, kamien lub nozyce")
b=input()

while True: 
    if a=="papier" and b=="papier":
        print(a)
        print("remis")
    elif a=="kamien" and b=="kamien":
        print(a)
        print("remis")
    elif a=="nozyce" and b=="nozyce":
        print(a)
        print("remis")
    elif a=="papier" and b=="kamien":
        print(a)
        print("przegrana")
    elif a=="papier" and b=="nozyce":
        print(a)
        print("wygrana")
    elif a=="kamien" and b=="papier":
        print(a)
        print("wygrana")
    elif a=="kamien" and b=="nozyce":
        print(a)
        print("przegrana")
    elif a=="nozyce" and b=="papier":
        print(a)
        print("przegrana")
    elif a=="nozyce" and b=="kamien":
        print(a)
        print("wygrana")

    #wygrane<3 or przegrane<3 
    
    #wygrane==3 or przegrane==3 
    #break
    
