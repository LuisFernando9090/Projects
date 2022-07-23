class MySingleton(type):
    _instances = {}

    def __call__(mySingletonClass, *args, **kwds):
        if mySingletonClass not in mySingletonClass._instances:
            instance = super().__call__(*args, **kwds)
            mySingletonClass._instances[mySingletonClass] = instance
        return mySingletonClass._instances[mySingletonClass]


class MySingletonTest(metaclass=MySingleton):
    _userLogin = ""
    _userPass = ""

    def __init__(self, login, password) -> None:
        self._userLogin = login
        self._userPass = password

    def set_userLogin(self, login):
        self._userLogin = login

    def set_Pass(self, password):
        self.set_Pass = password

    def get_userLogin(self):
        return self._userLogin

    def get_userPass(self):
        return self._userPass

myTest_1 = MySingletonTest("Sif", 123)
myTest_2 = MySingletonTest("Luis", 469)

if myTest_1 == myTest_2:
    print("Error: Login or Password are equals!")
else:
    print("Login Successfully!")
