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
    print("Das ist die " + str(fib(get_input())) + ". Stelle der Fibonacci-Folge.")