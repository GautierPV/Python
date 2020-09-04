#15
liste =[17, 38, 10, 25, 72]
tri=sorted(liste)
print (tri)
tri.append(12)
print(tri)
tri.reverse()
print(tri)
print(tri.index(17))
tri.remove(38)
print(tri)
print(tri[1:3])
print(tri[:2])
print(tri[2:])
for i in range(0,len(liste)+1):
    for j in range(i+1, len(liste)+1):
        print(liste[i:j])

#16

print(input("inverse le mot")[::-1])

#17

mot=(input("palindrome?"))
if mot == mot[::-1]:
    print("c'est un palindrome")
else:
    print("il ne s'agit pas d'un palindrome")

#18
adresse = input("adresse?")

if ("@" in adresse) and ("." in adresse) and (adresse[-4]=="."):
    print("email valide")
else:
    print("email invalide")

#19

truc=[]
machin=[None]*5
print(truc)
print(machin)

#20
for i in range(0,4):
    print(i)
for j in range(4,8):
    print(j)
for x in range(2,9):
    if(x%2==0):
        print(x)

chose=[]
for l in range(0,6):
    chose.append(l)

for d in range(3,7):
    if d in chose:
        print(str(d) + " est présent dans la liste")


