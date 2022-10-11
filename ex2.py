class Bank:
    def __init__(self):
        self.__accounts = []
        pass

    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self,accounts):
        if type(accounts) in (tuple,set,list):
            for i in accounts:
                self.__accounts.append(i)
        else:
            self.__accounts.append(i)
    
    def __has_Account (self,accounts):
        for i in self.__accounts:
            if accounts.cust.name == i.cust.name:
                print('you already have an account')
        return False

class Account:
    def __init__(self, no, cust):
        self.no = no
        self.cust = cust

    @property
    def no(self):
        return self.__no

    @no.setter
    def no(self,no):
        self.__no = no

    @property
    def cust(self):
        return self.__cust
    
    @cust.setter
    def cust(self,cust):
        self.__cust = cust

    def __repr__(self) -> str:
        return str(self.__dict__)

class Customer:
    def __init__(self, name, age):
        self.name = name
        if age < 18:
            print('fbi open up')
            pass
        else:
            print('customer was made')
            self.age = age
        

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def acc(self):
        self.__acc

    @acc.setter
    def acc(self,acc):
        self.__acc = acc
