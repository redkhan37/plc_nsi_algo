class File1:
    """ File implémentée sur la base d'une liste chainée simple"""
    from algo.struct.liste_simple import Liste

    def __init__(self):
        pass

    def __len__(self):
        pass

    def enfiler(self, valeur):
        """ à faire """
        pass

    def defiler(self):
        """ à faire """
        pass

    def __str__(self):
        pass


class File2:
    """ File implémentée sur la base d'une deque (file double) python """
    from collections import deque

    def __init__(self):
        pass

    def __len__(self):
        pass

    def enfiler(self, valeur):
        """ à faire """
        pass

    def defiler(self):
        """ à faire """
        pass

    def __str__(self):
        pass


class File3:
    """ File implémentée sur la base de deux piles."""
    from algo.struct.piles import Pile1 as Pile

    def __init__(self):
        pass

    def __len__(self):
        pass

    def enfiler(self, valeur):
        """ à faire """
        pass

    def defiler(self):
        """ à faire """
        pass

    def __str__(self):
        pass


class File4:
    """ File implémentée sur la base d'un tableau de taille fixe.
    Pour cela, on prend une list python mais on s'interdit les méthodes
    append, pop, insert. 
    """

    def __init__(self, taille=1024):
        pass
