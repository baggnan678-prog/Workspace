notes = [{"prenom":"Moussa","note":8},{"prenom":"Bitié","note":4},{"prenom":"Sogotele","note":1},{"prenom":"Ali","note":10},{"prenom":"Yirako","note":10},{"prenom":"Lala","note":1},{"prenom":"Irie","note":3},{"prenom":"Zirio","note":5},{"prenom":"Luffy","note":6},{"prenom":"Son","note":7},{"prenom":"Alicia","note":9},{"prenom":"Rene","note":4},{"prenom":"Sali","note":10},{"prenom":"Paco","note":3}]
somme = 0
for i in notes:
    somme+=i["note"]
print(f"La moyenne est : {somme/len(notes)}")
sup5=[a for a in notes if a["note"]>5]
print(f"Les notes suprieures ou égales à 5 sont : {list(a["note"] for a in sup5)}")
inf4=[a["note"] for a in notes if a["note"]<4]
print(f"Les notes infrieures ou égales à 4 sont : {inf4}")
print(f"La pire note obtenue est {min([a["note"] for a in notes])}")
print(f"le nom des clients ayant donné de faibles notes sont : {list(a["prenom"] for a in notes if a["note"]<4)}") 