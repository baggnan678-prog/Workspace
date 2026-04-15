import math
import statistics
limite=int(input("Combien de note il y as t'il : "))
note = [int(input("entrer une note : ")) for a in range(limite)]
def moyenne_gen(note):
    return sum(note)/len(note)
def max_gen(note):
     max(note)
def min_gen(note):
     min(note)
def min_gen(note):
    return min(note)
def moyenne_geo(note):
    return statistics.mean(note)
def ecart_type(note):
    return statistics.stdev(note)
best = [a for a in note if a >= 15]
lose = [a for a in note if a < 5 ]
print(f"La moyenne générale est {moyenne_gen(note)}")
print(f"La note la plus élevée est {max_gen(note)}")
print(f"La note la plus basse est {min_gen(note)}")
print(f"La moyenne géométrique est {moyenne_geo(note)}")
print(f"L'écart type est {ecart_type(note)}")
print(f"Les meilleures notes sont {best}")
print(f"Les notes les plus basses sont {lose}")