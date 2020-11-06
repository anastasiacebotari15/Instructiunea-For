"""Utilizînd ciclul FOR elaboraţi un program care să calculeze suma numerelor de la 1 la n, 
care se împart la 3 şi 5 pentru oricare n întrodus de la tastatură."""
a=eval(input("a="))
s=0
for i in range(1,a,1):
    if ((i%3==0) and (i%5==0)) :
        s+=i
print("Suma numerelor este", s)