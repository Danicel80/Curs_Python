# try:
#     file = open("file.txt", "r")
#     print(file.read())
# except:
#     print("Error managing file")
# finally:
#     file.close()
#
# with open("file.txt", "r") as file:
#     print(file.read())
#
#
# import time
# from functools import wraps
#
#
# def logger(functia_originala):
#     @wraps(functia_originala)
#     def wrapper(*args):
#         result = functia_originala(*args)
#         return result, args
#     return wrapper
#
#
# def timeit(functia_originala):
#     @wraps(functia_originala)
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = functia_originala(*args, **kwargs)
#         t2 = time.time() - t1
#         print(t2)
#         return result
#     return wrapper
#
#
# @logger
# def calculate(a, b):
#     return a + b
#
#
# print(calculate(2, 4))
from decor import add_border


class User:
    name = ""
    email = ""
    b_date = ""
    password = ""
    _logged_in = False

    def __init__(self, name, email, password, b_date):
        self.name = name
        self.email = email
        self.password = password
        self.b_date = b_date
        print(f"Welcome {name}, your account was created, please login")

    def login(self, name, password):
        if self.name == name and self.password == password:
            self._logged_in = True
            print(f"Welcome {name}")
        else:
            self._logged_in = False
            print(f"Sorry {name}, wrong login data")

    def logout(self):
        if self._logged_in:
            self._logged_in = False
            print("Goodbye")

    @staticmethod
    def require_login(function):
        def login_wrap(*args, **kwargs):
            function(*args, **kwargs)
        return login_wrap
    
    @add_border
    @require_login
    def get_info(self):
        if self._logged_in:
            print(self.name)
            print(self.email)
            print(self.b_date)
        else:
            print("You must be logged in to use this function")


x = User("Tanta", "tanta@yahoo.com", "12345", "12-01-1399")
x.get_info()
x.login("Tanta", "12345")
x.get_info()
