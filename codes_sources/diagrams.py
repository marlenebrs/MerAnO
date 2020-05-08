import requests
import pandas as pd
import numpy as np
# To install pandas: conda install pandas
import pylab as plt
import json


# Excel file
myFile = '/Users/marlenebarus/Master1/Semestre8/PdP/eggnog/Lactobacillus/query_seqs.fa.emapper.annotations'

############################# 1 - Génère la liste des modules présent dans un fichier d'annotations #############################
def list_modules(fichier_annotations):
    csv = pd.read_csv(fichier_annotations, sep="\t", header=3, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

    modules = []
    for i in range(len(csv)):
        temp = csv['KEGG_Module'][i]                          # stocke le contenu de chaque case de la colonne 'KEGG_Module' dans une variable temporaire
        if not pd.isnull(temp):                               # Si la valeur est différente de "NaN"
            value = str(csv['KEGG_Module'][i]).split(",")     # Pour les cases composées de plusieurs id de modules -> coupe au niveau de la virgule et stocke dans une liste
            for word in value:
                modules.append(word)

    return modules

modules_list = list_modules(myFile)
print(modules_list)

############################# 2 - On vérifie si les modules sont présents dans le fichier JSON : check_json(module) #############################

############################# 3 - Création de la fonction qui va mettre à jour le fichier JSON : update_json(dict_module) #############################

############################# 4 - Si pas dans JSON alors on requête KEGG : request_kegg(liste_modules) #############################

def request_kegg(module):        #### Fonction en cours de création faites pas attention :D
        r = requests.get('http://rest.kegg.jp/find/module/%s' % module)
        data = r.text
        if data != '\n':
            data = data.strip('\n')
            data = data.strip('md:')
            data = data.replace('\t','  ')

    return data


# Création d'un fichier JSON contenant le dictionnaire des id de modules associés à leur nom

#with open("modules.json","w") as f:
#    f.write(json.dumps(list_dico, indent=4))

############################# 5 - On va créer une liste générale data qui va contenir tous les grands modules pathways  #############################


