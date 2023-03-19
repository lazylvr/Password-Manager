import string
import random

def generate_password(longueur=12):
    """
    Génère un mot de passe aléatoire avec la longueur spécifiée.

    Args:
        longueur (int): La longueur du mot de passe. La valeur par défaut est 12.

    Returns:
        str: Le mot de passe généré.
    """
    lettres = string.ascii_letters
    chiffres = string.digits
    symboles = string.punctuation

    # Combinez tous les caractères pour former la liste des caractères autorisés
    caracteres_autorises = lettres + chiffres + symboles

    # Mélangez la liste des caractères autorisés
    caracteres_melanges = random.sample(caracteres_autorises, len(caracteres_autorises))

    # Sélectionnez des caractères dans la liste des caractères mélangés pour former le mot de passe
    mot_de_passe = ''.join(random.choice(caracteres_melanges) for _ in range(longueur))

    return mot_de_passe
