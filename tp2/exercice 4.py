tab=[int(input("entré une note : ")) for _ in range(6)]
tableau2 = [paire*2 for paire in tab ]
tableau3 = [paire  if paire%2!=0 else 0 for paire in tab]

print (f"Voici le tableau {tab} , voici la liste en multipliant les valeur obtenues par 2 {tableau2}, voici les valeurs en rajoutant les 0 à la place des nombres paires {tableau3}")

