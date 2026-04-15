def Moyenne(T):
    t2=[a for a in T if a%2==0]
    return sum(t2)/len(t2)
T=[]
for i in range (5):
    x=int(input('entrer un nombre :'))
    T.append(x)
print(Moyenne(T))

    