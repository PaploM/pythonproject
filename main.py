from Auth_controller.app_auth import app_auth
from model.Client import Client
from utils.utils import App_Utils



def get_input_from_user(app_auth=App_Auth):
    name=input("Enter Client Name: ")
    id=input("Enter Client Id: ")
    age=input("Enter Client Age: ")
    id_no=input("Enter Client id_no: ")
    phone_number = input("Enter Client  Phone_number: ")
    if App_Utils.check_value_is_empty(name,id,age,id_no,phone_number):
        print("Invaild Inputs")
        return


    Cli=Client(name=name,id=auth.get_last_id()+1,age=age,id_no=id_no)
    app_auth.register_new_Client(Cli)

print("Welcome, Please add your credival: ")
user_name = input("Username: ")
password = input("password: ")

if App_Utils.check_value_is_empty(user_name,password):
    print("Empty fields")
    exit()

auth = app_auth()
if auth.login(user_name,password):
   print("What you want to do: \n 1_add new client.\n 2_Search from user by id ")
   emp_choise=input("User choise: ")
   if not App_Utils.check_value_is_empty(emp_choise):
       if emp_choise=="1":
           get_input_from_user(auth)
