import utilisateur
from exceptions import *


class Dataset:
    def __init__(self, id_dataset, nom, source, taille_mo, type_donnees, proprietaire):

        if not isinstance(proprietaire, utilisateur.Utilisateur):
            raise TypeError("Le propriétaire doit être une instance de la classe Utilisateur.")

        if taille_mo <= 0:
            raise TailleDatasetInvalideException(
                f"La taille {taille_mo} n'est pas valide, elle doit être positive."
            )

        types_autorises = ["JSON", "CSV", "SQL", "IMAGE", "LOG"]
        if type_donnees not in types_autorises:
            raise TypeDatasetInvalideException(
                f"Le type '{type_donnees}' n'est pas supporté."
            )

        self.id_dataset = id_dataset
        self.nom = nom
        self.source = source
        self.taille_mo = taille_mo
        self.type_donnees = type_donnees
        self.proprietaire = proprietaire

    def afficher_infos(self):
        print(
            f"=== Informations ===\n"
            f"ID        : {self.id_dataset}\n"
            f"Nom       : {self.nom}\n"
            f"Source    : {self.source}\n"
            f"Taille    : {self.taille_mo} Mo\n"
            f"Type      : {self.type_donnees}\n"
            f"Propriétaire : {self.proprietaire.nom} (Rôle : {self.proprietaire.role})"
        )

    def est_volumineux(self, seuil=1000):
        if self.taille_mo > seuil:
            print(f"Attention : le dataset '{self.nom}' est volumineux.")
            return True
        return False

    def __str__(self):
        return (f"{self.id_dataset} | {self.nom} | {self.source} "
                f"| {self.taille_mo} Mo | {self.type_donnees}")