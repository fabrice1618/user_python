from classes.User import User
from classes.UserRole import UserRole

def main():
    # Exemple d'utilisation de la classe User et UserRole
    user = User(login="john_doe", password="password123", role=UserRole.ADMIN)
    print("Nom d'utilisateur :", user.login)
    print("Mot de passe haché :", user.pwd_hash)
    print("Rôle de l'utilisateur :", user.role)

if __name__ == "__main__":
    main()
