depenses=[int(input("entré une dépense : ")) for _ in range(6)]
total=sum(depenses)
moyenne=total/len(depenses)
max=max(depenses)
min=min(depenses)
depense_limiter=[dep for dep in depenses if dep>2000]
print (f"Voici le tableau des dépenses {depenses} , voici le total des dépenses {total} , voici la moyenne des dépenses {moyenne} , voici la dépense maximale {max} , voici la dépense minimale {min} , voici les dépenses supérieures à 2000 {depense_limiter}")