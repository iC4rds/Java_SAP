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