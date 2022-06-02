## Python Projects

### Fibonacci Folge

```markdown
def get_input():
    while True:
        Z = input("Gib eine Zahl an!  ")
        try:
            Z = int(Z)
            return Z
        except ValueError:
            print("Das ist keine Zahl!")
            get_input()

def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1)+fib(n-2)

#def f(L=None):
    #if L is None:
        #L = []
    #L.append(fib(get_input()))
    #return L

if __name__ == "__main__":
    print("Das ist die " + str(fib(get_input())) + ". Stelle der Fibonacci-Folge."
```

### Temperatur umwandeln

```markdown
def get_temp():
    while True:
        T = input("Gib die Temperatur an! ")
        try:
            T = float(T)
            return T
        except ValueError:
            print("Das ist keine Temperatur!")

def F_to_C_and_K():
    F = get_temp()
    F = F - 32
    C = 5/9 * F
    K = C + 273.15
    print("Das sind " + str(C) + " Grad Celsius")
    print("und " + str(K) + " Kelvin")

def C_to_F_and_K():
    C = get_temp()
    K = C + 273.15
    C = C + 17.8
    F = 9/5 * C
    print("Das sind " + str(F) + " Grad Fahrenheit")
    print("und " + str(K) + " Kelvin")

def temperaturskala():
    ddd = input("Welche Temperaturskala möchtest du umwandeln? Gib F für Fahrenheit und C für Celsius an! ")
    if ddd == str("F"):
        F_to_C_and_K()
    elif ddd == str("C"):
        C_to_F_and_K()
    else:
        print("Entweder F oder C!")
        temperaturskala()

temperaturskala()
```

### mit Rest dividieren

```markdown
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
```
