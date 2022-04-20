class Lebewesen:
    augen = 3

    def __init__(self):
        self.klasse = "säuger"

    def lebe(self):
        self.augen = 4
        return self.augen

class Hund(Lebewesen):
    beine = 42
    name = "Fiffi"

    def __init__(self):
        Lebewesen.__init__(self)
        Lebewesen.lebe(self)
        Hund.lebe(self)
        self.list = []

    def do_something(self, neuezahl):
        self.augen = neuezahl

    def lebe(self):
        self.beine = 43

fiffi = Hund()
print(str(fiffi.name) + " hat " + str(fiffi.augen) + " Augen!")
print(fiffi.klasse)
print(fiffi.beine)