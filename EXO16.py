print("Entrer deux mots de la même longueure")
mot1 = input("Premier mot : ")
mot2 = input("Deuxieme mot : ")
nombre_lettre = len(mot1)

#Fontion distance hamming
def distance_hamming(var1,var2) :
    compteur = 0
    for x in range (nombre_lettre) :
        if var1[x] != var2[x] :
            compteur += 1
    print (compteur)

#On vérifie que les deux mots sont de la même longueur, si oui on execute la fonction
if len(mot1) == len(mot2) :
    distance_hamming(mot1,mot2)
else :
    print("Vous devez entrer deux mots de la même longueur !")