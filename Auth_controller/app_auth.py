from model import Client
from model.Librarian import Librarian
from utils.utils import Constants
class app_auth:Librarian_list : list[Librarian] =[
         Librarian(1,"Mohammed Khaled",26,"200",Constants.FALL_TIME,"Mohammed","147852"),
         Librarian(2, "Bahaa Mohammed", 20,"201" , Constants.PART_TIME, "Bahaa", "369852")]


client_list: list[Client] = [(1, "Khaled", 30, "123","0591234")]

def get_last_id(self):
    return self.client_list[len(self.client_list) - 1].get_id()

def login(self, username: str, password: str)-> bool:
        for item in self.librarians_list:
                if username == item.get_username() and password == item.get_password():
                        return True
                return False

def register_new_user(self,user:Librarian):
    if not self.check_if_user_exsist(user.get_user_name()):
           self.Librarians_list.append(user)
    else:
        print("User already Used!")
        print(len(self.client_list))


def register_new_Client(self,user:Client):
        if not self.check_if_user_exsist(user.get_user_name()):
                self. client_list.append(user)
        else:
            print("User already Used!")



def check_if_user_exsist(self,username:str):
     for item in self.Librarians_list:
         if item.get_username()==username:
                 return True
         return False


