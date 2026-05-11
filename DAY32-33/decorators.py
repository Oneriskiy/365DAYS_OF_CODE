# import time
#
# def decorator(func):
#     def wrapper():
#         print('start')
#
#         func()
#
#         print('end')
#
#     return wrapper
#
# @decorator
# def hello():
#     print('hello')
#
# hello()
#
#
# def login_decor(login):
#     def wrapper():
#         print('func started')
#
#         login()
#         print('func ended')
#
#     return wrapper
#
#
# @login_decor
# def login():
#     print("Logging user...")
#     time.sleep(1)
#     print("successful")
#
# login()
#
# #time decorator
# def timer(load):
#     def wrapper():
#         start = time.time()
#
#         load()
#
#         end = time.time()
#
#         print(end - start)
#
#     return wrapper
#
# @timer
# def load():
#     for i in range(10):
#         print(i)

user_data = {'status': 'admin'}

def admin_check(func):
    def wrapper(*args, **kwargs):
        user_data = kwargs.get('status')
        if user_data != 'admin':
            print('bye')
            return

        result = func(*args, **kwargs)
        print('successful')
        return result

    return wrapper

@admin_check
def register(**kwargs):
    user = 'admin'
    print("welcome")
    return user

register(status=user_data['status'])