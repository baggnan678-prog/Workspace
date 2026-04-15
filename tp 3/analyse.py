import scipy
def moyenne (d):
    somme=0
    for i in d:
        somme+=i["note"]
    return somme/len(d)

def moyenne_geo(d):
    d=[a["note"] for a in d]
    return scipy.stats.gmean(d)

def meilleurNotation (d):
    sup5=[a["note"] for a in d if a["note"]>5]
    return sup5

def mauvaiseNotation (d):
    inf4=[a["note"] for a in d if a["note"]<4]
    return inf4

def pireNote (d):
    return [a["prenom"] for a in d if a["note"]<3]