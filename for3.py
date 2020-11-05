"""Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele pare, pentru 
intervalul de la 1 la n (n-este citit de la tastatură)."""
a=eval(input("a="))
b=0
for i in range(2,a,2):
    b+=2
    print(i)