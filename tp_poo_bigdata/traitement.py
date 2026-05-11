import dataset


class Traitement:
    def __init__(self, id_traitement, nom_traitement, dataset):
        self.id_traitement = id_traitement
        self.nom_traitement = nom_traitement
        self.dataset = dataset

    def executer(self):
        raise  NotImplementedError("Cette methode doit etre redefini par les classe fille.")

class NettoyageDonnees(Traitement):
    def executer(self):
        print(f"___________[Nettoyage] Execution sur  '{self.dataset.nom()}'__________")
        print(f"Suppression des doublans et nettoyage des valeurs manquantes termines.")

class TransformationDonnees(Traitement):
    def executer(self):
        print(f"--- [Transformation] Exécution sur '{self.dataset.nom}' ---")
        print("Normalisation des données et encodage terminés.")

class AnalyseStatistique(Traitement):
    def executer(self):
        print(f"--- [Analyse] Exécution sur '{self.dataset.nom}' ---")
        print(f"Moyenne, Médiane et Écart-type calculés pour {self.dataset.nom}.")
        