# Fonction Recherche_suspect
def recherche_suspect(ADN, nom, code_1, code_2) :
    if (ADN.find(code_1) and ADN.find(code_2)!= -1) and (ADN.find(code_1) - ADN.find(code_2) > 4) :
        return nom + " est coupable ! On retrouve ses brains d'ADN " + code_1 + " et " + code_2 + " dans sa séquence ADN."
    else :
        return nom + " n'est pas  coupable."
    
# Execution de la fonction pour les 4 suspects, avec les paramètres ADN, NOM, CODE 1 et 2
print(recherche_suspect("CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCADN","Moutarde","CATA","ATGC"))
print(recherche_suspect("CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGADN","Rose","CATA","ATGC"))
print(recherche_suspect("AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCCADN","Pervenche","CATA","ATGC")) 
print(recherche_suspect("CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG","Leblanc","CATA","ATGC"))
