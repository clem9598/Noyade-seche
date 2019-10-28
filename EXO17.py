# Fonction Palyndrome
def palyndrome(var1) :
    if var1[::] == var1[::-1] :
        print  (mot, "est un palyndrome.")
    else :
        print (mot, "n'est pas un palyndrome.")
        
start = True

#Boucle pour rejouer 
while start : 
  reponse = input("Voulez vous jouer (o/n) ?")
  if reponse == "o" or reponse =="O" :
    mot = input("Entrer un mot : ")
    palyndrome(mot) # Execution de la fonction
  else : 
    start = False 

