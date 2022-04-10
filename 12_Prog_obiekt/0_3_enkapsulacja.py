class Account:
    def __init__(self, first_name, last_name):
        self.fist_name = first_name
        sefl.last_name = last_name
        self.__account_number = "12 345432443333333"

    def show_number(self):
        print (self.last_name, '--->')
        print ("Current number: {}".format(self.__account_number))

    def set_new_bank_number(self,number):
        self.__account_number=number
wiesniewska = Account()