from utils import users

class UsersPermissions:

    def __init__(self, permissions):
        self.__permissions = permissions

    @property
    def permissions(self):
        return self.__permissions

    def output(self):
        return f"{self.permissions}"

    def __repr__(self):
        return f"permission | {self.permissions}"


class Users(UsersPermissions):
    def __init__(self, user, permissions):
        super().__init__(permissions)
        self.__user = user

    @property
    def user(self):
        return self.__user


    def output(self):
        return f"{self.user} | {self.permissions}"

if __name__ == "__main__":
    user_permissions = Users(users[1], 'no')
    print(user_permissions.output())