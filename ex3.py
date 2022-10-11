
class Machine:

    def __init__(self):
        self._is_on = False

    def power_on(self):
        self._is_on = not False

class Printer(Machine):
    def __init__(self):
        Machine.__init__(self)
        self.__pt = Papertray()

    def print (self,text):
        if self.__pt.paper >= 1:
            if self._is_on:
                print(text)
                self.__pt.paper = self.__pt.paper - 1
            else:
                print('printer is off')
        else:
            print('No more paper')

    @property
    def loade(self):
        return self.__pt.paper

    @loade.setter
    def loade(self, paper):
        self.__pt.paper = paper

class Papertray:
    def __init__(self):
        self.paper = 2

    @property
    def paper(self):
        return self.__paper

    @paper.setter
    def paper(self, paper):
        self.__paper = paper

pr = Printer()
pa = Papertray
pr.print('hejsa')
pr.power_on()
pr.print('hejsa')
pr.print('hejsa')
pr.print('hejsa')
pr.loade
pr.print('hejsa')