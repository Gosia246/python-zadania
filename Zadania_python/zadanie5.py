a=float(input("Podaj dlugosc pierwszego boku: \n"))
b=float(input("Podaj dlugosc drugiego boku: \n"))
c=float(input("Podaj dlugosc trzeciego boku: \n"))

if a+b>c and b+c>a and a+c>b:
    print("Ten trojkat istnieje.")
else :
    print("Ten trojkat nie istnieje.")