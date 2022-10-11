
class Car():
    def __init__(self, make, model, bhp, mhp):
        self.make = make
        self.model = model
        self.bhp = bhp
        self.mhp = mhp
        
    @property
    def make(self):
        return self.__make
    @make.setter
    def make(self,make):
        self.__make = make

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self,model):
        self.__model = model

    @property
    def bhp(self):
        return self.__bhp
    @bhp.setter
    def bhp(self,bhp):
        self.__bhp = bhp

    @property
    def mhp(self):
        return self.__mhp
    @mhp.setter
    def mhp(self,mhp):
        self.__mhp = mhp

    def __repr__(self):
        return f'{self.__dict__}'

car1 = Car('hejsa','test',22, 100)
car1.make = 'test'
print(car1)