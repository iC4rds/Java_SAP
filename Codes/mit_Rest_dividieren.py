def get_input_a():
    while True:
        v = input("Durch welche Zahl möchtest du dividieren?  ")
        try:
            a = int(v)
            return a
        except ValueError:
           print("Das ist keine Zahl")

def get_input_m():
    while True:
        va = input("Womit?  ")
        try:
            m = int(va)
            return m
        except ValueError:
            print("Das ist keine Zahl")

def get_input_b():
    while True:
        var = input("Was ist der Rest?  ")
        try:
            b = int(var)
            return b
        except ValueError:
            print("Das ist keine Zahl")

def mod():
    a = get_input_a()
    m = get_input_m()
    b = get_input_b()
    r = a%m
    if r == b:
        print("Das ist richtig")
    else:
        print("Nein, der Rest ist " + str(r))

mod()