class ABR:
    """Représentation de la structure abstraite des arbres binaires de recherche.
    Un arbre binaire vide sera représenté par None.
    Attributs:
        valeur : la valeur de la racine de l'arbre
        sag : le sous-arbre gauche, de type ABR, vide par défaut
        sad : le sous-arbre droit, de type ABR, vide par défaut
    Méthodes:
        get_valeur : renvoie la valeur de la racine
        get_gauche : renvoie le sous-arbre gauche
        get_droit : renvoie le sous-arbre droit
        inserer : ajoute un noeud à l'arbre, dont l'étiquette est la valeur donnée.
    """

    def __init__(self, valeur):
        """
        Paramètre:
            valeur : la valeur de la racine de l'arbre
        """
        self.valeur = valeur
        self.sag = None
        self.sad = None

    def get_valeur(self):
        """Méthode qui renvoie la valeur de la racine de l'arbre."""
        return self.valeur

    def get_gauche(self):
        """Méthode qui renvoie le sous-arbre gauche de l'arbre."""
        return self.sag

    def get_droit(self):
        """Méthode qui renvoie le sous-arbre droit de l'arbre."""
        return self.sad

    def inserer(self, valeur):
        """Méthode qui ajoute un noeud à l'arbre, dont l'étiquette est la valeur donnée.
        Paramètre:
            valeur : l'étiquette du noeud
        """
        if self == None:               # L'arbre est vide
            self = ABR(valeur)
        else:
            if valeur < self.valeur:   # la valeur est inférieure à celle de la racine
                if self.sag == None:   # le sous arbre gauche est vide
                    self.sag = ABR(valeur)
                else:
                    self.sag.inserer(valeur)
            else:                      # la valeur est supérieure à celle de la racine
                if self.sad == None:   # le sous arbre droit est vide
                    self.sad = ABR(valeur)
                else:
                    self.sad.inserer(valeur)

def afficher(arbre):
    """Fonction permettant de représenter l'arbre binaire sous la forme d'un
    tableau comprenant la valeur de sa racine, le sous-arbre gauche et
    le sous-arbre droit.
    Paramètre:
        arbre : instance de la classe ABR
    Sortie:
        un tableau : list
    """
    if arbre != None:
        return [arbre.get_valeur(), afficher(arbre.get_gauche()), afficher(arbre.get_droit())]