arabigos = [(1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")]

def arabigo_a_romano(num):
    resultado = ""

    for valor, letra in arabigos:
        while num >= valor:
            resultado += letra
            num -= valor

    return resultado

romanos = {"M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1}

def romano_a_arabigo(num):
    resultado = 0

    for i in range(len(num) - 1):
        if romanos[num[i]] < romanos[num[i + 1]]:
            resultado -= romanos[num[i]]
        else:
            resultado += romanos[num[i]]

    resultado += romanos[num[-1]]

    return resultado

lineas = []

while True:
    try:
        lineas.append(input())
    except EOFError:
        break

for linea in lineas:
    if linea.isdigit():
        print(arabigo_a_romano(int(linea)))
    else:
        print(romano_a_arabigo(linea))