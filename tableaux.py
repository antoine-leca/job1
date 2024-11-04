##----- job 1

def fruits():
    fruits = ["pomme", "cerise", "orange"]
    return print(fruits)

fruits()

##----- job 2

def fruits():
    fruits = ["pomme", "cerise", "orange"]
    return print(fruits[1])

fruits()

##----- job 3

def fruits(add):
    fruits = ["pomme", "cerise", "orange"]
    fruits.append(add)
    return print(fruits)

fruits("Melon")

##----- job 4

def fruits(add):
    fruits = ["pomme", "cerise", "orange", "melon"]
    fruits.insert(2, add)
    return print(fruits)

fruits("mangue")

##----- job 5

L= [1, 2, 3 , 4 , 5]
print(L)
print(L[1])
def lm(L):
    L[3] = L[2] + L[4]
    print(L)
    print(L[-1])
lm(L)

##----- job 6

L2 = [1, 2, 3, 4, 5]
print("Liste de base : ", L2)
L2[0], L2[-1] = L2[-1], L2[0]
print("Liste modifiée : ", L2 )

##----- job 7

div = 3
L3 = [8, 24, 48, 2 , 16]

def nombDiv(L3, div):
    i = 0
    for x in L3:
        if x % div ==0:
            i = i + 1
    return i

print("Le nombre d'éléments de L3 qui sont divisibles par", div, "est", nombDiv(L3,div) )

##----- job 8

L4 = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
sum_even = sum(x for x in L4 if x % 2 == 0)
print("La somme des valeurs paires est : ", sum_even)

##----- job 9

L5 = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
print("La valeur max est : ", max(L5))
print("La valeur min est : ", min(L5))

##----- job 10

L6 = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
l6 = []
i = 1

for c1 in L6:
    if c1 in range(25, 90):
        l6.append(c1)

for val in l6:
    i = i * val

print(l6)
print(i)

##----- job 11

L7 = [7, 11, 42, 39, 2]
print("Liste de base : ", L7)
L7 = [x+1 for x in L7]
print("Liste +1 : ", L7)

##----- job 12

L88=[76,23,45,12,54,9] 
print("Liste de base : ", L88)
for b in range(len(L88)):
    for w in range(b+1, len(L88)): 
        if L88[b] > L88[w]: L88[b], L88[w] = L88[w], L88[b]

print("Liste par ordre croissant : ", L88)

##----- Job 13

L9 = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print("Liste de base : ", L9)

L9 = [x for i, x in enumerate(L9) if x not in L9[:i]]
print("Liste sans doublons : ", L9)

