import hashlib
import string
from classes.UserRole import UserRole

class User:
    """
    Classe User
    """
    def __init__(self, id=None, login=None, pwd_hash=None, role=None):
        self.id = id
        self.login = login
        self.pwd_hash = pwd_hash
        self.role = role

    @classmethod
    def from_tuple(cls, data):
        if data is None:
            return None
        id, login, pwd_hash, role = data
        return cls(id=id, login=login, pwd_hash=pwd_hash, role=role)

    # Mutator / Accessor
    @property
    def id(self): 
        return self._id

    @id.setter
    def id(self, id):
        if id is None:
            self._id = None
        elif User.validate_id(id):
            self._id = id
        else:
            raise ValueError(f"Erreur valeur id: type={type(id)}, valeur={id}")

    @property
    def login(self):
        return self._login
        
    @login.setter
    def login(self, login):
        if login is None:
            self._login = None
        if User.validate_login(login):
            self._login = login
        else:
            raise ValueError(f"Erreur valeur login: type={type(login)}, valeur=\'{login}\'")

    @property
    def pwd_hash(self):
        return self._pwd_hash

    @pwd_hash.setter
    def pwd_hash(self, pwd_hash):
        if pwd_hash is None:
            self._pwd_hash = None
        elif self.validate_pwd_hash(pwd_hash):
            self._pwd_hash = pwd_hash
        else:
            raise ValueError(f"Erreur valeur pwd_hash: type={type(pwd_hash)}, value=\'{pwd_hash}\'")

    def set_password(self, password):
        if password is None:
            self._pwd_hash = None
        elif User.validate_password(password):
            self._pwd_hash = User.__hash_password(password)
        else:
            raise ValueError(f"Erreur valeur password: type={type(password)}, value=\'{password}\'")
        
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        if role is None:
            self._role = None
        elif UserRole.validate_role(role):
            self._role = role
        elif isinstance(role, str):
            self._role = UserRole.from_str(role)
        else:
            raise ValueError(f"Erreur valeur role: type={type(role)}, valeur=\'{role}\'")

    @property
    def role_str(self):
        return UserRole.role_str(self._role)

    # Méthodes de validation de champs
    @staticmethod
    def validate_id(id):
        if isinstance(id, int) and id > 0:
            return True
        return False

    @staticmethod
    def validate_login(login):
        if  not isinstance(login, str) or \
            len(login) == 0 or \
            len(login) > 20:
            return False
        
        for lettre in login:
            if not lettre in User.lettres_acceptees():
                return False

        return True

    @staticmethod
    def lettres_acceptees():
        lettres_acceptees = "!#€£µ§$%&*+-./:<=>?@_|~"
        lettres_acceptees += "éèàùâêîôûçäïëöüÿ"
        lettres_acceptees += string.ascii_letters
        lettres_acceptees += string.digits
        return lettres_acceptees

    # Méthodes password
    @staticmethod
    def validate_pwd_hash(pwd_hash):
        if  not isinstance(pwd_hash, str) or \
            len(pwd_hash) != 64:
            return False
        for lettre in pwd_hash:
            if not lettre in string.hexdigits:
                return False
        return True

    @staticmethod
    def validate_password(password):
        if  not isinstance(password, str) or \
            len(password) == 0 or \
            len(password) > 20:
            return False
        for lettre in password:
            if not lettre in User.lettres_acceptees():
                return False
        return True

    def verify_password(self, password):
        hashed_password = self.__hash_password(password)
        return (self._pwd_hash == hashed_password)

    @staticmethod
    def __hash_password(password):
        password_bytes = password.encode('utf-8')
        hashed_password = hashlib.sha256(password_bytes).hexdigest()
        return hashed_password

    # __repr__ et validation objet
    def __repr__(self):
        return f"User(id={self._id}, login={self._login}, pwd_hash={self.pwd_hash}, role={self.role_str})"
    
    @staticmethod
    def is_valid(user):
        if user.login is not None and \
            user.pwd_hash is not None and \
            user.role  is not None:
            return True
        return False