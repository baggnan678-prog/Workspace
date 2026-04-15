tab=[int(input("entré un âge : ")) for _ in range(6)]
tableau2 = [âge for âge in tab if âge>=18]
tableau3 = [âges for âges in tab if âges<18]
print (f"Voici le tableau des âges {tab} , voici les âges des personnes majeures {tableau2} , voici les âges des personnes mineures {tableau3}")
