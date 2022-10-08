class Person:
    def __init__(self, id, full_name, age, id_no,user_name="",password=""):
        self.__id = id
        self.__full_name = full_name
        self.__age = age
        self.__id_no = id_no
        self.__user_name = user_name
        self.__password = password

    def get_id(self):
        return self.get.__id

    def get_user_name(self):
        return self.get.__user_name

    def get_passsword (self):
        return self.get.__passsword

