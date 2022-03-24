x=float(input("Podaj wspolrzedna x: "))
y=float(input("Podaj wspolrzedna y:"))

if x>0 and y>0 :
    print(f"Punkt {(x,y)} znajduje sie w 1 cwiartce")
elif x<0 and y>0 :
    print(f"Punkt {(x,y)} znajduje sie w 2 cwiartce")
elif x<0 and y<0 :
    print(f"Punkt {(x,y)} znajduje sie w 3 cwiartce")
elif x>0 and y<0 :
    print(f"Punkt {(x,y)} znajduje sie w 4 cwiartce")