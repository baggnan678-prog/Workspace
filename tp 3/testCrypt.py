# =============================================================================
# MODULE : testCrypt.py
# RÔLE   : Programme principal pour tester le cryptage et le décryptage
# AUTEUR : TP Génie Logiciel 1 – UTM
# =============================================================================

# On importe les deux fonctions définies dans notre module "crypt.py".
# Le mot "from" indique depuis quel fichier on importe.
# Le mot "import" indique quelles fonctions on veut utiliser.
# Grâce à cet import, on peut appeler crypt() et decrypt() directement
# sans avoir besoin d'écrire "crypt.crypt()" ou "crypt.decrypt()".
from crypt import crypt, decrypt


# =============================================================================
# FONCTION UTILITAIRE : afficher_separation()
# =============================================================================
# Cette petite fonction affiche simplement une ligne de tirets pour séparer
# visuellement les différentes sections dans la console.
# C'est une bonne pratique d'avoir des fonctions même pour de petites tâches
# répétitives : cela évite de copier-coller du code.
# =============================================================================
def afficher_separation():
    """Affiche une ligne de séparation visuelle dans la console."""
    # print() affiche du texte dans la console et passe à la ligne suivante.
    # On affiche 50 tirets "-" pour créer une ligne horizontale.
    print("-" * 50)  # "-" * 50 = "--------------------------------------------------"


# =============================================================================
# FONCTION PRINCIPALE : main()
# =============================================================================
# Par convention, on regroupe le code principal dans une fonction appelée
# "main" (mot anglais signifiant "principal"). Cela rend le code plus
# organisé et réutilisable.
# =============================================================================
def main():
    """Programme principal : teste le cryptage et décryptage de mots de passe."""

    # ------------------------------------------------------------------
    # EN-TÊTE : Affichage du titre du programme
    # ------------------------------------------------------------------
    print("=" * 50)                          # Ligne de séparation haute
    print("   CRYPTAGE / DÉCRYPTAGE DE MOT DE PASSE")  # Titre centré
    print("=" * 50)                          # Ligne de séparation basse

    # ------------------------------------------------------------------
    # PARTIE 1 : Test avec l'exemple donné dans le sujet du TP
    # ------------------------------------------------------------------
    # On définit le mot de passe de l'exemple du TP.
    # Les guillemets doubles " " délimitent une chaîne de caractères (str).
    mdp_exemple = "epi_Sogo1@"

    # f-string : les f-strings permettent d'insérer des variables directement
    # dans une chaîne de caractères, entre accolades {}.
    # Exemple : f"Bonjour {nom}" affichera "Bonjour Ali" si nom = "Ali"
    print(f"\n[Exemple du TP] Mot de passe original : '{mdp_exemple}'")
    afficher_separation()

    # --- CRYPTAGE ---
    # On appelle la fonction crypt() qui retourne un TUPLE (deux valeurs).
    # Python permet de "dépackager" un tuple directement :
    #   code, cle = crypt(mdp_exemple)
    # est équivalent à :
    #   resultat = crypt(mdp_exemple)
    #   code = resultat[0]
    #   cle  = resultat[1]
    code, cle = crypt(mdp_exemple)

    # Affichage du résultat du cryptage
    # ' '.join(code) : joint tous les éléments de la liste "code" en une seule
    # chaîne, séparés par un espace ' '.
    # Exemple : ['65', '70', '69'] → "65 70 69"
    print(f"Code hexadécimal (mélangé) : {' '.join(code)}")

    # Affichage de la clé (liste d'indices)
    print(f"Clé (indices d'origine)    : {cle}")

    # --- DÉCRYPTAGE ---
    # On appelle la fonction decrypt() avec le code et la clé produits
    # par crypt(). Elle doit nous redonner exactement le mot de passe original.
    mdp_retrouve = decrypt(code, cle)

    # Affichage du mot de passe retrouvé
    print(f"Mot de passe décrypté      : '{mdp_retrouve}'")

    # Vérification : on compare le mot de passe retrouvé avec l'original.
    # L'opérateur == retourne True si les deux valeurs sont identiques, False sinon.
    # On affiche directement le résultat booléen (True ou False).
    print(f"Décryptage réussi          : {mdp_retrouve == mdp_exemple}")

    # ------------------------------------------------------------------
    # PARTIE 2 : Test interactif avec la saisie de l'utilisateur
    # ------------------------------------------------------------------
    afficher_separation()

    # input() affiche un message et attend que l'utilisateur tape quelque chose
    # et appuie sur Entrée. La valeur saisie est stockée dans la variable.
    mdp_saisi = input("\nEntrez votre mot de passe à crypter : ")

    # --- CRYPTAGE du mot de passe saisi ---
    code2, cle2 = crypt(mdp_saisi)

    # Affichage des résultats
    print(f"\nCode hexadécimal (mélangé) : {' '.join(code2)}")
    print(f"Clé                        : {cle2}")

    # --- DÉCRYPTAGE du mot de passe saisi ---
    mdp_retrouve2 = decrypt(code2, cle2)
    print(f"Mot de passe décrypté      : '{mdp_retrouve2}'")
    print(f"Décryptage réussi          : {mdp_retrouve2 == mdp_saisi}")

    # Ligne de fin pour fermer visuellement le programme
    print("=" * 50)


# =============================================================================
# POINT D'ENTRÉE DU PROGRAMME
# =============================================================================
# En Python, chaque fichier possède une variable spéciale appelée __name__.
# Quand on EXÉCUTE directement ce fichier (python testCrypt.py),
# Python met automatiquement __name__ = "__main__".
# Quand ce fichier est IMPORTÉ depuis un autre fichier,
# Python met __name__ = "testCrypt" (le nom du fichier).
#
# Cette condition permet donc de n'exécuter le code principal QUE si on
# lance ce fichier directement, pas si on l'importe depuis ailleurs.
# C'est une bonne pratique très répandue en Python.
# =============================================================================
if __name__ == "__main__":
    # On appelle la fonction principale pour démarrer le programme
    main()
