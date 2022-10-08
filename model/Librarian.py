from model.person import Person
class Librarian (Person):
    def __init__(self ,id,full_name,age,id_no, emplyment_type,user_name,passwod):
        self.__emplyment_type = emplyment_type
        self.__user_name = user_name
        self.__password=passwod


def get_id(self):
    return self.__id


def get_full_name(self):
    return self.__full_name


def get_age(self):
    return self.__age


def get_id_no(self):
    return self.__id_no


def get_phone_number(self):
    return self.__phone_number

def get_emplyment_type(self):
    return self.__emplyment_type

def get_user_name(self):
    return self.__user_name

def get_passwod(self):
    return self.__password

