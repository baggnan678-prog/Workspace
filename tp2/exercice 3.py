tab=[int(input("entré une note : ")) for _ in range(6)]
tableau2 = [paire for paire in tab if paire%2==0]
tableau3 = [paires for paires in tab if paires%2!=0]
print (f"Voici le tableau {tab} , voici la somme {sum(tab)} , voici les nombres paires {tableau2} , voici les nombres impaires {tableau3}")
