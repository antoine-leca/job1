##job 1/2/3
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)

##job 3/4
a = "abcdefghijklmnopqrstuvwxyz"
print(a)
print(a[::-1])

##job 06
ma_string = "Je suis une String"
print(ma_string)

##job 7
num1 = 40
num2 = 2
print(num1+num2)

##job 8
num3 = 3
num4 = 14
print(num3*num4)

##job 9
nom1 = "Bouteilles d'eau"
prix_u1 = 2
qu1 = 2

print(nom1, " Prix/u : ", prix_u1, " Quantité : ", qu1)

prix_u2 = (prix_u1*0.1)

achat = int(input("Combien souhaitez-vous en acheter ? "))
print(int(achat) + qu1)

qu1 = qu1 + achat

print(prix_u1)

prix_u1 = (prix_u1+prix_u2)
print(prix_u1)

print(nom1, " Prix/u : ", prix_u1, " Quantité : ", qu1)

##job 10
i = 5000
taux = 4/100

gain1 = i*taux
print(i + gain1)

taux = taux + 2/100
add = 5000
i = i + gain1 + add

gain2 = i*taux
i = i + gain2
print(i)

retrait = i*10/100
i = i - retrait
taux = taux - 1/100
print(i)

gain3 = i*taux
i = i + gain3
print(i)

#+
chaine = input("Ecrivez une phrase : ")
print(chaine.count("e"))
