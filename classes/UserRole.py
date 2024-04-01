from enum import Enum

class UserRole(Enum):
    GUEST = 'guest'
    USER = 'user'
    ADMIN = 'admin'

    @staticmethod
    def validate_role(role):
        return isinstance(role, UserRole)

    @staticmethod
    def role_str(role_type):
        for role in UserRole:
            if role_type == role:
                return role.value
        return None

    @staticmethod
    def from_str(role_str):
        for role in UserRole:
            if role_str == role.value:
                return role
        return None
