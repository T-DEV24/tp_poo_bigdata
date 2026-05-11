from dataset import Dataset, DatasetIntrouvableException


class GestionnaireDataset:
    def __init__(self):
        self.datasets = []

    def ajouter_dataset(self, nouveau_dataset):
        if not isinstance(nouveau_dataset, Dataset):
            raise TypeError("L'objet doit être une instance de la classe Dataset.")
        self.datasets.append(nouveau_dataset)
        print(f"Dataset '{nouveau_dataset.nom}' ajouté avec succès.")

    def afficher_datasets(self):
        if not self.datasets:
            print("Aucun dataset enregistré.")
            return
        for ds in self.datasets:
            ds.afficher_infos()

    def rechercher_par_id(self, id_dataset):
        for ds in self.datasets:
            if ds.id_dataset == id_dataset:
                return ds
        raise DatasetIntrouvableException(
            f"Dataset avec l'ID {id_dataset} introuvable."
        )

    def supprimer_dataset(self, id_dataset):
        ds = self.rechercher_par_id(id_dataset)
        self.datasets.remove(ds)
        print(f"Dataset '{ds.nom}' supprimé avec succès.")

    def filtrer_par_type(self, type_donnees):
        resultat = [ds for ds in self.datasets if ds.type_donnees == type_donnees]
        if not resultat:
            print(f"Aucun dataset de type '{type_donnees}' trouvé.")
        return resultat

    def calculer_taille_totale(self):
        totale = sum(ds.taille_mo for ds in self.datasets)
        return f"{totale:.2f} Mo"

    def afficher_datasets_volumineux(self):
        print("=== Datasets volumineux (> 1000 Mo) ===")
        volumineux = [ds for ds in self.datasets if ds.taille_mo >= 1000]
        if not volumineux:
            print("Aucun dataset volumineux trouvé.")
            return
        for ds in volumineux:
            ds.afficher_infos()