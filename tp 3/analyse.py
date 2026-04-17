import scipy
def moyenne (d):
    valeur=list(d.values())
    return    sum(valeur)/len(d) 


def moyenne_geo(d):
    d=[a for a in d.values()]
    return scipy.stats.gmean(d)

def meilleurNotation(d):
    sup5=[a for a in d.values() if a > 5]
    return sup5

def mauvaiseNotation (d):
    inf4=[a for a in d.values() if a<4]
    return inf4

def pireNote (d):
    return [nom for nom , a in d.items() if a<4]