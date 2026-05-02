with open("notes.txt", "w") as f:
    f.write("Ali;14\nAwa;16\nMoussa;9\nFatou;12\nIssa;18\n")

etudiants = []
with open("notes.txt", "r") as f:
    for ligne in f:
        nom, note = ligne.strip().split(";")
        etudiants.append((nom, int(note)))

for nom, note in etudiants:
    print(f"{nom} : {note}")

moyenne = sum(n for _, n in etudiants) / len(etudiants)
print(f"\nMoyenne : {moyenne:.2f}")

meilleure = max(n for _, n in etudiants)
print(f"Meilleure note : {meilleure}")

print("\nÉtudiants admis :")
admis = [(nom, note) for nom, note in etudiants if note >= 10]
for nom, note in admis:
    print(f"  {nom} : {note}")

with open("admis.txt", "w") as f:
    f.write("Nom;Note\n")
    for nom, note in admis:
        f.write(f"{nom} {note}\n")
with open('notes2.json','w') as f:
    json.dump(etudiants,f,indent=4)
    print("\nDonnées enregistrées au format JSON.")
