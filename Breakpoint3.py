#6
adresse = input("adresse?")

if ("@" in adresse) and (adresse[-4:]==".com"):
        print("email valide")

#7
for i in range(10):
    print("ceci est une boucle lol")

#8

for i in "patate":
    print(i)

#9

a=0
b=10

for a in range(b+1):
    print(a)

#9

while b!=0:
    if b%2==0:
        print(b)
    b-=1

#11

saisie=11
while saisie<1 or saisie>10:
    saisie=int(input("rentrez une saisie de 1 à 10"))

#12

for i in "patate":
    print(i)

gundam = ["uwu","owo","umu","QAQ"]

for i in gundam:
    print(gundam[i])

#13

for i in range(0,15):
    if (i%3==0):
        print(i)

#14

nombre=int(input("nombre?"))
n=0
while n !=nombre:
    if (n%2==0):
        print(n)
    n+=1

for i in range(nombre):
    if (i%2==0):
        print(i)