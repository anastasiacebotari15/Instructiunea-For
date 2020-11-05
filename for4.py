"""Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele impare, pentru 
intervalul de la a la b (a și b se citesc de la tastatură)."""
a=eval(input("Introduceti a="))
b=eval(input("Introduceti b="))
if a%2!=0:
    for c in range(a,b+1,2):
        print(c)
if a%2==0:
    for c in range(a+1,b+1,2):
        print(c) 
