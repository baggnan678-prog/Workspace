produit=[str(input("entré un mot : ")) for _ in range(4)]
verification = str(input("entré un mot à vérifier : "))
verif=produit.count(verification)
if verif==0:
    print (f"Voici le tableau {produit} , voici le mot à vérifier {verification} , et le mot n'est pas present")
else:
    index=produit.index(verification)
    print (f"Voici le tableau {produit} , voici le mot à vérifier {verification} , et le mot est present {verif} fois à l'index {index}")
