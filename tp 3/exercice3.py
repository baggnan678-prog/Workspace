notation = [{"prenom":"Moussa","note":8},{"prenom":"Bitié","note":4},{"prenom":"Sogotele","note":1},{"prenom":"Ali","note":10},{"prenom":"Yirako","note":10},{"prenom":"Lala","note":1},{"prenom":"Irie","note":3},{"prenom":"Zirio","note":5},{"prenom":"Luffy","note":6},{"prenom":"Son","note":7},{"prenom":"Alicia","note":9},{"prenom":"Rene","note":4},{"prenom":"Sali","note":10},{"prenom":"Paco","note":3}]
import analyse
print(f"La moyenne est : {analyse.moyenne (notation)}")
print(f"Les notes suprieures ou égales à 5 sont : {analyse.meilleurNotation(notation)}")
print(f"Les notes infrieures ou égales à 4 sont : {analyse.mauvaiseNotation(notation)}")
print(f"le nom des clients ayant donné de faibles notes sont : {analyse.pireNote(notation)}") 
print(f"La moyenne géométrique est : {analyse.moyenne_geo(notation)}")