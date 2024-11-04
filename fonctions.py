##----- job 1

def myprintHello():
    print("Hello World")

myprintHello()

##----- job 2 

def myprintName(Name):
    print(Name)

myprintName("Antoine")
myprintName("Alexandre")
myprintName("Balqisse")
myprintName("Emilie")

##----- job 3

def add(n1, n2):
    print(n1 + n2)

add(1,1)
add(2,2)
add(3,3)

##----- job 4

def getHello():
    return print("Hello La Plateforme")

getHello()

##----- job 5

def calcul(num1, operator, num2):
    if operator == "+" :
        return print("Résultat : ", num1 + num2)
    elif operator == "-":
        return print("Résultat : ", num1 - num2)
    elif operator == "*":
        return print("Résultat : ", num1 * num2)
    elif operator == "/":
        return print("Résultat : ", num1 / num2)
    elif operator == "%":
        return print("Résultat : ", num1 % num2)
    else:
        print("Veuillez renseigner un opérateur.")

calcul(2, "+", 2)
calcul(2, "-", 2)
calcul(2, "*", 2)
calcul(2, "/", 2)
calcul(2, "%", 2)
calcul(2, 0 , 2)

##----- job 6

def pn(nombre1):
    if nombre1 < 0:
        print("négatif")
    elif nombre1 > 0:
        print("positif")
    else:
        print("neutre")

pn(-1)
pn(0)
pn(1)

##----- job 7

def lg(langage):
    if langage == "JavaScript":
        print("Vous êtes un développeur web.")
    elif langage == "Python":
        print("Vous êtes un développeur IA.")
    elif langage == "Java":
        print("Vous êtes un développeur logiciel.")
    elif langage == "ReactJS":
        print("Vous êtes un développeur mobile.")
    else:
        print()

lg("JavaScript")
lg("Python")
lg("Java")
lg("ReactJS")

##----- job 8

def s(type, saison):
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi.") 
    elif type == "fruits" and saison == "été":
        print("Poire, fraise, cassis.")
    elif type == "légumes" and saison == "hiver":
        print("Carotte, topinambour, endive.")
    elif type == "légumes" and saison == "été":
        print("Artichaud, aubergine, navet.")
    else:
        print()

s("fruits", "hiver")
s("fruits", "été")
s("légumes", "hiver")
s("légumes", "été")

##----- job 9

note1 = int(input("Saisissez la première note : "))
note2 = int(input("Saisissez la deuxième note : "))
note3 = int(input("Saisissez la troisième note : "))

def av(note1, note2, note3):
    
    average = ((note1 + note2 + note3)/3) 
    print(average)

    if average in range(15, 20):
        print("Très bon élève.")
    elif average in range(11, 14):
        print("Bon élève.")
    elif average in range(8, 10):
        print("Elève moyen.")
    elif average in range(0, 7):
        print("Elève devant faire des efforts")
    else:
        print()

av(note1, note2, note3)

##----- job 10

def pi(nombrepi):
    if type(nombrepi) == int and nombrepi> 0:
        if nombrepi %2 == 0:
            print("Le nombre est pair.")
        else:
            print("Le nombre est impair.")
    else:
        print("Veuillez enter un nombre entier et supérieur à 0.")
    

pi(24)
pi(25)
pi(-1)
pi(25.5)

##----- job 11
nem = int(input("Renseignez un nombre : "))

def ttt(nem):
    heure = nem/60
    minute = nem%60
    if nem < 120:
        print(int(heure), "heure et", minute, "minutes.")
    elif nem > 120:
        print(int(heure), "heures et", minute, "minutes.")
    elif nem < 120 and minute < 2:
        print(int(heure), "heure et", minute, "minute.")
    elif nem > 120 and minute > 1:
            print(int(heure), "heures et", minute, "minutes.")
    else:
        print()

ttt(nem)

##----- +
inm = input("Renseignez un mot : ")

def an(inm):
    print(inm[::-1])

an(inm)