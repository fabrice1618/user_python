# Programme principal
from classes.Db import Db
from classes.Users import Users
from classes.User import User
from classes.UserRole import UserRole

# Connexion à la base de données
Db.open('/data/database.db')

user1 = Users.read(1)
print("read id=1: ", user1)

user2 = Users.read(2)
print("read id=2: ", user2)

id = Users.find_login('Pilon_charles')
if id is not None:
    user3 = Users.read(id)
    print(f"read id={id}: ", user3)

    Users.delete(id)
    print("user deleted")
else:
    new_user = User(login='Pilon_charles', pwd_hash=None, role=UserRole.GUEST)
    new_user.set_password("password1234")
    Users.create(new_user)
    print("utilisateur ajouté:", new_user)

users = Users.index()
print("index", type(users), users)

print("index_generator:")
for user in Users.index_generator():
    print(user.login)

Db.close()
