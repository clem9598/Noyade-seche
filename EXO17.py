mot = input("Entrer un mot : ")
nombre_lettre = len(mot)

# Fonction Palyndrome
def palyndrome(var1) :
    if var1[::] == var1[::-1] :
        print  (mot, "est un palyndrome.")
    else :
        print (mot, "n'est pas un palyndrome.")

# Execution de la fonction
palyndrome(mot)