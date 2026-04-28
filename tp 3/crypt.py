# =============================================================================
# MODULE : crypt.py
# RÔLE   : Contient les fonctions de cryptage et décryptage d'un mot de passe
# =============================================================================

# On importe le module "random" qui permet de faire des opérations aléatoires
# (comme mélanger une liste). Ce module fait partie de la bibliothèque standard
# de Python, donc pas besoin de l'installer.
import random


# =============================================================================
# FONCTION UTILITAIRE : to_hex(elt)
# =============================================================================
# Une fonction "utilitaire" est une petite fonction d'aide utilisée par
# d'autres fonctions. Ici, elle convertit UN caractère en code hexadécimal.
# QU'EST-CE QUE L'HEXADÉCIMAL ?
# Le système hexadécimal (base 16) utilise les chiffres 0-9 et les lettres
# a-f. Chaque caractère du clavier possède un code numérique (appelé code
# ASCII ou Unicode). Par exemple :
#   - 'e' → code 101 en décimal → '65' en hexadécimal
#   - 'A' → code 65  en décimal → '41' en hexadécimal
# C'est une façon standard de représenter des données en informatique.
# =============================================================================
def to_hex(elt):
    """
    Convertit un caractère en sa représentation hexadécimale.

    Paramètre :
        elt (str) : un caractère (ex: 'e', 'A', '@')

    Retourne :
        str : la représentation hexadécimale du caractère (ex: '65', '41', '40')
    """
    # .encode('utf-8') : convertit le caractère en une séquence d'octets
    # selon le standard UTF-8 (le standard d'encodage le plus utilisé au monde)
    s = elt.encode('utf-8')

    # .hex() : convertit ces octets en une chaîne hexadécimale lisible
    # Exemple : 'e'.encode('utf-8') → b'\x65' → .hex() → '65'
    return s.hex()


# =============================================================================
# FONCTION PRINCIPALE 1 : crypt(mdp)
# =============================================================================
# Cette fonction réalise le CRYPTAGE du mot de passe en 4 étapes :
#   Étape 1 → Convertir chaque caractère en hexadécimal
#   Étape 2 → Créer une liste d'indices (numéros de position d'origine)
#   Étape 3 → Mélanger aléatoirement ces indices
#   Étape 4 → Réorganiser les codes hex selon le nouvel ordre des indices
#
# EXEMPLE avec le mot de passe "epi_Sogo1@" (10 caractères) :
#   Étape 1 → hex_list   = ['65','70','69','5f','53','6f','67','6f','31','40']
#   Étape 2 → indices    = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#   Étape 3 → après shuffle : indices = [2, 7, 5, 1, 3, 4, 6, 8, 9, 0]
#   Étape 4 → code_final = ['69','6f','6f','70','5f','53','67','31','40','65']
#             (on a pris hex_list[2], hex_list[7], hex_list[5], etc.)
# =============================================================================
def crypt(mdp):
    """
    Crypte un mot de passe selon l'algorithme hexadécimal + mélange aléatoire.

    Paramètre :
        mdp (str) : le mot de passe à crypter (ex: "epi_Sogo1@")

    Retourne :
        tuple : (code_final, cle)
            - code_final (list) : liste des codes hexadécimaux mélangés
            - cle (list)        : liste des indices d'origine (sert à décrypter)
    """

    # ------------------------------------------------------------------
    # ÉTAPE 1 : Conversion de chaque caractère en hexadécimal
    # ------------------------------------------------------------------
    # On utilise une "liste en compréhension" (list comprehension) :
    # c'est une façon compacte de créer une liste en Python.
    #
    # Version longue équivalente (plus lisible pour un débutant) :
    #   hex_list = []               ← on crée une liste vide
    #   for c in mdp:               ← on parcourt chaque caractère du mot de passe
    #       hex_list.append(to_hex(c))  ← on ajoute son code hex à la liste
    #
    # La version compacte (list comprehension) fait exactement pareil :
    hex_list = [to_hex(c) for c in mdp]
    # Exemple : "epi" → ['65', '70', '69']

    # ------------------------------------------------------------------
    # ÉTAPE 2 : Créer la liste des indices d'origine
    # ------------------------------------------------------------------
    # len(mdp) → donne la longueur du mot de passe (nombre de caractères)
    # range(n) → génère les entiers de 0 à n-1
    # list(...) → convertit ce range en une vraie liste Python
    #
    # Exemple : len("epi_Sogo1@") = 10
    # → range(10) = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # → indices   = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    indices = list(range(len(mdp)))

    # ------------------------------------------------------------------
    # ÉTAPE 3 : Mélanger les indices aléatoirement
    # ------------------------------------------------------------------
    # random.shuffle() mélange la liste EN PLACE, c'est-à-dire qu'elle
    # modifie directement la liste "indices" sans en créer une nouvelle.
    # Le résultat est différent à chaque exécution (caractère aléatoire).
    #
    # Exemple avant shuffle : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Exemple après  shuffle : [2, 7, 5, 1, 3, 4, 6, 8, 9, 0]  ← aléatoire
    random.shuffle(indices)

    # ------------------------------------------------------------------
    # ÉTAPE 4 : Réorganiser les codes hex selon les nouveaux indices
    # ------------------------------------------------------------------
    # On reconstruit une nouvelle liste en allant chercher les codes hex
    # dans l'ordre donné par "indices".
    #
    # Exemple : indices = [2, 7, 5, 1, ...]
    #   → code_final[0] = hex_list[2] = '69'  (le 3e caractère 'i')
    #   → code_final[1] = hex_list[7] = '6f'  (le 8e caractère 'o')
    #   → code_final[2] = hex_list[5] = '6f'  (le 6e caractère 'o')
    #   → code_final[3] = hex_list[1] = '70'  (le 2e caractère 'p')
    #   ... etc.
    #
    # Version longue équivalente :
    #   code_final = []
    #   for i in indices:
    #       code_final.append(hex_list[i])
    code_final = [hex_list[i] for i in indices]

    # La CLÉ = les indices dans leur ordre mélangé.
    # IMPORTANT : sans cette clé, il est IMPOSSIBLE de décrypter le message.
    # C'est le "secret" partagé entre l'expéditeur et le destinataire.
    # Exemple : cle = [2, 7, 5, 1, 3, 4, 6, 8, 9, 0]
    cle = indices

    # On retourne un TUPLE (une paire de valeurs groupées).
    # L'appelant pourra récupérer les deux valeurs séparément ainsi :
    #   code, cle = crypt("monMDP")
    return code_final, cle


# =============================================================================
# FONCTION PRINCIPALE 2 : decrypt(code, key)
# =============================================================================
# Cette fonction réalise l'opération INVERSE du cryptage.
# Elle a besoin des DEUX éléments produits par crypt() :
#   - le code (liste des hex mélangés)
#   - la clé (liste des indices d'origine)
#
# PRINCIPE :
#   Lors du cryptage, on a déplacé chaque code hex de sa position d'origine
#   vers une nouvelle position. La clé enregistre ces déplacements.
#   Pour décrypter, on fait le chemin inverse : on remet chaque code
#   à sa position d'origine grâce à la clé.
#
# EXEMPLE :
#   code = ['69','6f','6f','70','5f','53','67','31','40','65']
#   key  = [2, 7, 5, 1, 3, 4, 6, 8, 9, 0]
#
#   Lecture de la clé :
#   → key[0]=2 : le code[0]='69' devait être à la position 2 → hex_original[2]='69'
#   → key[1]=7 : le code[1]='6f' devait être à la position 7 → hex_original[7]='6f'
#   → key[2]=5 : le code[2]='6f' devait être à la position 5 → hex_original[5]='6f'
#   ... etc.
#
#   hex_original = ['65','70','69','5f','53','6f','67','6f','31','40']
#   → décodage   → "epi_Sogo1@"   ✓
# =============================================================================
def decrypt(code, key):
    """
    Décrypte un code hexadécimal en utilisant la clé de cryptage.

    Paramètres :
        code (list) : liste des codes hexadécimaux mélangés (produit par crypt)
        key  (list) : liste des indices d'origine (la clé produite par crypt)

    Retourne :
        str : le mot de passe original reconstruit
    """

    # ------------------------------------------------------------------
    # ÉTAPE 1 : Créer un tableau vide de la bonne taille
    # ------------------------------------------------------------------
    # On prépare une liste remplie de chaînes vides '', avec autant
    # d'emplacements qu'il y a de codes hexadécimaux.
    #
    # Exemple : len(code) = 10
    # → hex_original = ['', '', '', '', '', '', '', '', '', '']
    #
    # Cette liste servira à recevoir les codes remis en ordre.
    hex_original = [''] * len(code)

    # ------------------------------------------------------------------
    # ÉTAPE 2 : Replacer chaque code à sa position d'origine
    # ------------------------------------------------------------------
    # enumerate(key) parcourt la liste key en donnant simultanément :
    #   - position_melangee : l'index actuel dans la liste "key" (0, 1, 2, ...)
    #   - position_origine  : la valeur stockée dans key à cet index
    #
    # Exemple avec key = [2, 7, 5, 1, ...] :
    #   - tour 1 : position_melangee=0, position_origine=2
    #     → hex_original[2] = code[0] = '69'
    #     (le 1er élément du code mélangé reprend la place numéro 2)
    #   - tour 2 : position_melangee=1, position_origine=7
    #     → hex_original[7] = code[1] = '6f'
    #   - tour 3 : position_melangee=2, position_origine=5
    #     → hex_original[5] = code[2] = '6f'
    #   ... et ainsi de suite pour tous les éléments
    for position_melangee, position_origine in enumerate(key):
        hex_original[position_origine] = code[position_melangee]

    # ------------------------------------------------------------------
    # ÉTAPE 3 : Décoder chaque code hexadécimal en caractère
    # ------------------------------------------------------------------
    # On commence avec une chaîne de caractères vide
    mdp = ''

    # On parcourt chaque code hexadécimal dans la liste restaurée
    for h in hex_original:
        # bytes.fromhex(h) : convertit la chaîne hexadécimale en objet bytes
        #   Exemple : bytes.fromhex('65') → b'\x65'
        # .decode('utf-8') : convertit cet objet bytes en caractère lisible
        #   Exemple : b'\x65'.decode('utf-8') → 'e'
        # += : concatène (ajoute) le caractère à la fin de la chaîne mdp
        mdp += bytes.fromhex(h).decode('utf-8')

    # ------------------------------------------------------------------
    # ÉTAPE 4 : Retourner le mot de passe reconstruit
    # ------------------------------------------------------------------
    # À ce stade, mdp contient tous les caractères dans l'ordre original.
    # Exemple : "epi_Sogo1@"
    return mdp
