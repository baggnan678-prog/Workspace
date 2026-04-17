notation =  { "Moussa" :8 , "Bitié" :4 , "Sogotele" :1 , "Ali" :10 , "Yirako" :10 , "Lala" :1 , "Irie" :3 , "Zirio" :5 , "Luffy" :6 , "Son" :7 , "Alicia" :9 , "Rene" :4 , "Sali" :10 , "Paco" :3} 
valeur=list(notation.values())
print(f"La moyenne est :  {sum(valeur)/len(notation) }")
sup5=[a for a in notation.values() if a > 5]
print(f"Les notation suprieures ou égales à 5 sont : {   sup5 }")
inf4=[a for a in notation.values() if a<4]
print(f"Les notation infrieures ou égales à 4 sont : {  inf4 }")
print(f"La pire notation obtenue est  {min(valeur)} ")
print(f"le nom des clients ayant donné de faibles notation sont :  { [nom for nom , a in notation.items() if a<4] }") 