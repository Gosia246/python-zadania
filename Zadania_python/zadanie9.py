print("Kalkulator BMI")
print("Podaj swoja wage w kg: ")
waga=float(input())
print("Podaj swoj wzrost w metrach: ")
wzrost=float(input())
BMI=waga/(wzrost*wzrost)
print("Twoje BMI wynosi", BMI)
if BMI<20:
    print("niedowaga")
elif 20<=BMI<25:
    print("waga prawidlowa")
elif  25<=BMI<30: 
    print("nadwaga")
elif BMI>=30:
    print("otylosc")