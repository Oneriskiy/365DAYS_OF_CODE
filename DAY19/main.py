from utils import *


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



def generator():
    for user in users.items():
        yield user


def menu(gen):
    for id, name in gen:
        print(f'{id}: {name}')
    permission_asc = int(input("Enter the user ID from the list: "))
    asc = input("Enable Administrator Privileges? ON | OFF: ").upper()
    if asc == 'ON':
        asc = ON
    elif asc == 'OFF':
        asc = OFF
    user_permissions = Users(users[permission_asc], users_permissions[asc])
    print(user_permissions.output())
if __name__ == "__main__":
    gen = generator()

    menu(gen)