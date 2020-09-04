import math

#1
temps = 6.892
distance = 19.7

vitesse = float(distance/temps)

print(round(vitesse, 1))

#2
nom = str(input("nom?"))

age = int(input("age ?"))

#3
flou = float(input("float ?"))

if flou>=0:
    print(math.sqrt(flou))
elif flou<0:
    print("veuillez entrer un positif")

#4

mot1 = input("mot1?")
mot2 = input("mot2?")

if mot1>mot2:
    print(mot2 +" est le plus petit")
elif mot2 > mot1:
    print(mot1 + " est le plus petit")

#5

pseuil = 2.3

vseuil = 7.41

pression = float(input("pression ?"))
volume = float(input("volume ?"))

if (pression > pseuil and volume > vseuil):
    print("arrêt immédiat")
elif (pression > pseuil and volume < vseuil):
    print("augmente le volume gamin")
elif (pression < pseuil and volume > vseuil):
    print("diminue le volume gamin")
elif (pression < pseuil and volume < vseuil):
    print("Tout est ok rien à signaler")