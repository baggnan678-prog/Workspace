etudiant = { "nom": "Issa", "age": 22, "notes": [12, 15, 14] }
print(f"Voici le nom de l'étudiant {etudiant['nom']}")
print(f"La moyenne de l'étudiant est de {sum(etudiant['notes'])/len(etudiant['notes'])}")
etudiant["notes"].append(16)
etudiant["age"]=23
etudiant["ville"]="Ouagadougou"
print(etudiant)