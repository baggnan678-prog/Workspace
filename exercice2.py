import math
def puissance(var1):
    return -1**var1+1
def factorielle(var1):
    return math.factorial(var1)
def equation (x,var1 , puissance,factorielle):
    var1=0
    p=puissance(var1)/factorielle(var1)*x**var1
    var1=var1+1
    return p+(equation(x,var1 , puissance,factorielle))
var1=0
x=int(input("entrer un nombre : "))
print (f"le résultat de l'équation est {equation(x,var1 , puissance,factorielle)}")
