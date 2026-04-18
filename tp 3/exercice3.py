notation =  { "Moussa" :8 , "Bitié" :4 , "Sogotele" :1 , "Ali" :10 , "Yirako" :10 , "Lala" :1 , "Irie" :3 , "Zirio" :5 , "Luffy" :6 , "Son" :7 , "Alicia" :9 , "Rene" :4 , "Sali" :10 , "Paco" :3} 
import analyse
print(f"La moyenne est : {analyse.moyenne (notation)}")
print(f"Les notes suprieures ou égales à 5 sont : {analyse.meilleurNotation(notation)}")
print(f"Les notes infrieures ou égales à 4 sont : {analyse.mauvaiseNotation(notation)}")
print(f"le nom des clients ayant donné de faibles notes sont : {analyse.pireNote(notation)}") 
print(f"La moyenne géométrique est  : {analyse.moyenne_geo(notation)}")