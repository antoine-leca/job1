##------ job 1
valeur1 = input("Renseignez une première valeur : ")
valeur2 = input("Renseignez une deuxième valeur : ")
if valeur1 == valeur2:
    print("Les valeurs sont égales.")
else:
    print("Les valeurs ne sont pas égales.")

##----- job 2
age = int(input("Quel âge avez-vous ? "))
if age >=18:
    print("Vous ne pouvez pas voter.")
else:
    print("Vous pouvez voter.")

##----- job 3
numbers1 = 1
while numbers1 <=100:
    if numbers1 == 26 or numbers1 == 37 or numbers1 == 88:
        print("")
    else:
        print(numbers1)
    numbers1 = numbers1 + 1

##----- job 4
numbers2 = 0
while numbers2 <=100:
    if numbers2%3 == 0 and numbers2%5 == 0 :
        print("FizzBuzz")
    elif numbers2%3 == 0 :
        print("Fizz")
    elif numbers2%5 == 0 :
        print("Buzz")
    else:
        print(numbers2)
    numbers2 +=1

##----- job 5
def nombrePremier(number):
    for n in range(2, number):
        if number % n == 0:
            return False
    return True
for x in range(2, 1000):
    if nombrePremier(x):
        print(x)

##----- job 6
n1 = int(input("Renseignez un nombre : "))
if (n1 % 2) == 0:
    print("{0} est pair.".format(n1))
else:
    print("{0} est impair.".format(n1))

##-----  job 7
alpha = "abcdefghijklmnopqrstuvwxyz" * 10
for ai in range(1, 31):
    print(alpha [0:ai+ai-1])

##----- job 8
ab = int(input("Premier côté du triangle (AB) : "))
bc = int(input("Deuxième côté du triangle (BC) : "))
ac = int(input("Troisième côté du triangle (AC) : "))
if ab < bc + ac and bc < ab + ac and ac < ab + bc:
    print("Le triangle AB = {}, BC = {}, AC = {} est constructible. ".format(ab, bc, ac))
else:
    print("Le triangle AB = {}, BC = {}, AC = {} n'est pas constructible, veuillez renseigner de nouvelles valeurs. ".format(ab, bc, ac))

isocele = ab == bc or bc == ac or ac == ab
rectangle = ab * ab + bc * bc == ac * ac or bc * bc + ac * ac == ab * ab or ac * ac + ab * ab == bc * bc

if ab == bc == ac:
    print("Ce triangle est équilatéral. ")

elif isocele and rectangle:
    print("Ce triangle est rectangle isocèle. ")

else:
    if isocele:
        print("Ce triangle est isocèle. ")
    elif rectangle:
        print("Ce triangle est rectangle. ")
    else:
        print("Ce triangle est quelconque. ")