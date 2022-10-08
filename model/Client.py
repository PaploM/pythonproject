from model.person import Person


class Client(Person):

    def __init__(self,id,full_name,age,id_no,phone_number):
        self.__phone_number = phone_number
        super(Client,self).__init__(id = id,full_name = full_name,age = age,id_no = id_no)

    def get_phone_number(self):
      return self.__phone_number