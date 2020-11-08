"""Să se calculeze sumele: 	s1=1+2+3+…+n
			s2=1*2+2*3+3*4+…+(n-1)*n
			s3=1+1*2+1*2*3+…+1*2*3*…*n
			s4=12+22+32+…+n2
			s5=1/2+2/3+3/4+…+n/(n+1)
			s6=1+2+22+23+24+…+2n
			Notă: Pentru fiecare sumă n – se va citi de la tastatură."""
n=eval(input("n="))
s1=0
for a in range(1,n+1):
    s1+=a
print("s1=", s1)
n=eval(input("n="))
s2=0
for b in range(1,n+1):
    s2+=((b-1)*b)
print("s2=", s2)
n=eval(input("n="))
s3=1
p=1
for c in range (1,n+1):
    p*=n
    s3+=p
print("s3=", s3)
n=eval(input("n="))
s4=0
for d in range (1,((n*10)+1)):
    s4+=d+2
print("s4=", s4)
n=eval(input("n="))
s5=0
for e in range (1,n+1):
    s5+=(e/(e+1))
print("s5=", s5)
n=eval(input("n="))
s6=0
for f in range(1,n):
    s6+=(20+n)
print("s6=", s6)