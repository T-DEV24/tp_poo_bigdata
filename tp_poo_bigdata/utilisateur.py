class Utilisateur:

    ROLES = ["Data Analyst" ,"Data engineer", "DBA", "Administrateur"]
    def __init__(self, id_user, nom, email, role):
        self.id_user = id_user
        self.nom = nom
        self.email = email
        self.role = role

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, valeur):
        if valeur not in self.ROLES:
            raise ValueError (f"Roles entrer invalide. choisissez parmi: {',' .join(self.ROLES)}")
        self._role = valeur

    def afficher_infos(self):
        print(f"====Profil utilisateur====: \n"
              f"ID: {self.id_user} \n"
              f"Nom: {self.nom} \n"
              f"Email: {self.email} \n"
              f"Role: {self.role}")

    def __str__(self) -> str:
        return f"{self.id_user} | {self.nom} | {self.email} | {self.role}"
