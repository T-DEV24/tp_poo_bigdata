from utilisateur import *
from dataset import *
from traitement import *
from gestionnaire_dataset import *


def afficher_menu():
    print("\n ===== MENU GESTION DATASETS =====")
    print("1. Ajouter un dataset")
    print("2. Afficher tous les datasets")
    print("3. Rechercher un dataset")
    print("4. Supprimer un dataset")
    print("5. Filtrer par type")
    print("6. Afficher les datasets volumineux")
    print("7. Calculer la taille totale")
    print("8. Lancer un traitement")
    print("0. Quitter")
    print()


def menu():
    gestionnaire = GestionnaireDataset()
    admin = Utilisateur(1, "admin1", "admin1@gmail.com", "Administrateur")

    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        try:
            if choix == "1":
                id_dataset = int(input("ID : "))
                nom = input("Nom : ")
                source = input("Source : ")
                taille = float(input("Taille (Mo) : "))
                type_d = input("Type (CSV, JSON, SQL, IMAGE, LOG) : ").upper()
                nouveau_dataset = Dataset(id_dataset, nom, source, taille, type_d, admin)
                gestionnaire.ajouter_dataset(nouveau_dataset)
                print(f"Dataset '{nom}' ajouté avec succès.")

            elif choix == "2":
                gestionnaire.afficher_datasets()

            elif choix == "3":
                id_dataset = int(input("ID : "))
                print(gestionnaire.rechercher_par_id(id_dataset))

            elif choix == "4":
                id_dataset = int(input("ID : "))
                gestionnaire.supprimer_dataset(id_dataset)

            elif choix == "5":
                type_d = input("Type à filtrer (CSV, JSON, SQL, IMAGE, LOG) : ")
                resultat = gestionnaire.filtrer_par_type(type_d)
                for r in resultat:
                    print(r)

            elif choix == "6":
                gestionnaire.afficher_datasets_volumineux()

            elif choix == "7":
                print(f"Taille totale : {gestionnaire.calculer_taille_totale()}")

            elif choix == "8":
                id_ds = int(input("ID du dataset à traiter : "))
                ds = gestionnaire.rechercher_par_id(id_ds)
                print("1. Nettoyage | 2. Transformation | 3. Analyse")
                t_choix = input("Type de traitement : ")

                if t_choix == "1":
                    NettoyageDonnees(1, "Nettoyage Standard", ds).executer()
                elif t_choix == "2":
                    TransformationDonnees(2, "Formatage", ds).executer()
                elif t_choix == "3":
                    AnalyseStatistique(3, "Stats", ds).executer()

            elif choix == "0":
                print("Au revoir")
                break

            else:
                print("Choix invalide.")

        except Exception as e:
            print(f"Erreur : {e}")


if __name__ == "__main__":
    menu()