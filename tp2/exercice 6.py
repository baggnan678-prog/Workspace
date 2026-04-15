tab=[int(input("entré une nombre : ")) for _ in range(5)]
tableau2 = sorted(tab)
print (f"Voici le tableau {tab} , voici la somme {sum(tab)} , voici les nombres triés {tableau2} , voici les nombres triés à l'envers {tableau2[::-1]}")