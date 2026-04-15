tab=[int(input("entré un nombre : ")) for _ in range(8)]
verification = int(input("entré un nombre à vérifier : "))
verif=tab.count(verification)
if verif==0:
    print (f"Voici le tableau {tab} , voici le nombre à vérifier {verification} , et le nombre n'est pas present")
else:
    print (f"Voici le tableau {tab} , voici le nombre à vérifier {verification} , et le nombre est present {verif} fois")