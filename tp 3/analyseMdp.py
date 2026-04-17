from collections import Counter

SPECIAL_CHARS = "$@!"


def check_password(mdp):
    if ("@" in mdp or "!" in mdp or "$" in mdp ) and any(c.isdigit() for c in mdp) and any(c.isupper() for c in mdp) and any(c.islower() for c in mdp) :
        return True
    else:
        return False


def lower_count(mdp: str) -> int:
    return sum(1 for c in mdp if c.islower())


def upper_count(mdp: str) -> int:
    return sum(1 for c in mdp if c.isupper())


def alphanum_count(mdp: str) -> int:
    return sum(1 for c in mdp if not c.isalpha())


def longest_upper(mdp: str) -> int:
    max_seq = cur_seq = 0
    for c in mdp:
        if c.isupper():
            cur_seq += 1
            if cur_seq > max_seq:
                max_seq = cur_seq
        else:
            cur_seq = 0
    return max_seq


def longest_lower(mdp: str) -> int:
    max_seq = cur_seq = 0
    for c in mdp:
        if c.islower():
            cur_seq += 1
            if cur_seq > max_seq:
                max_seq = cur_seq
        else:
            cur_seq = 0
    return max_seq


def bonus(mdp: str) -> int:
    pts = 0
    pts+=len(mdp)*4
    pts += upper_count(mdp)  * 2
    pts += lower_count(mdp)  * 3
    pts += sum(5 for c in mdp if ("@" in mdp or "!" in mdp or "$" in mdp))
    return pts


def penality(mdp: str) -> int:
    pen=0
    pen=longest_lower(mdp)*2 + longest_upper(mdp)*3
    return pen


def score(mdp: str) -> None:
    b    = bonus(mdp)
    p    = penality(mdp)
    s    = b - p
    ok   = check_password(mdp)

    print(f"  Mot de passe      : {mdp}")
    print(f"  Longueur          : {len(mdp)} caractères")
    print(f"  Valide            : {'Oui' if ok else 'Non'}")
    print(f"  Majuscules        : {upper_count(mdp)}")
    print(f"  Minuscules        : {lower_count(mdp)}")
    print(f"  Non-alphabétiques : {alphanum_count(mdp)}")
    print(f"  Séq. max MAJ      : {longest_upper(mdp)}")
    print(f"  Séq. max min      : {longest_lower(mdp)}")
    print(f"  Nombre de points pour la longueur : {len(mdp)*4}")
    print(f"  Nombre de points pour les majuscules : {upper_count(mdp)  * 2}")
    print(f"  Nombre de points pour les minuscules : {lower_count(mdp)  * 3}")
    print(f"  Nombre de points pour les non-alphabétiques : {sum(5 for c in mdp if ("@" in mdp or "!" in mdp or "$" in mdp))}")
    print(f"  Bonus             : +{b}")
    print(f"  Pénalité          : -{p}")
    print(f"  Score final     : {s}")
    if s>80:
        print("Mot de passe très fort")
    elif 80>s>=40:
        print("Mot de passe fort")
    elif 40>s>=20:
        print("Mot de passe Faible")
    else:
        print("Mot de passe très faible")
