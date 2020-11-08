"""Să se calculeze sumele: 	s1=1+2+3+…+n
			s2=1*2+2*3+3*4+…+(n-1)*n
			s3=1+1*2+1*2*3+…+1*2*3*…*n
			s4=12+22+32+…+n2
			s5=1/2+2/3+3/4+…+n/(n+1)
			s6=1+2+22+23+24+…+2n
			Notă: Pentru fiecare sumă n – se va citi de la tastatură."""
n=eval(input("n="))
s1=0
s2=0
s3=0
s4=0
s5=0
s6=0
for a in range(1,n+1):
    s1=s1+a
print("s1=", s1)
for b in range(1,n+1):
    s2=s2+((b-1)*b)
print("s2=", s2)
for d in range (1,n+1):
    s4=s4+((d*10)+2)
print("s4=", s4)
for e in range (1,n+1):
    s5=s5+(e/(e+1))
print("s5=", s5)