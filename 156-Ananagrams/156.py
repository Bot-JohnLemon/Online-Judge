lexico = []
copia = []
linea = input()

while linea != '#':
    palabras = linea.split()
    lexico += palabras
    for palabra in palabras:
        copia.append(sorted(list(palabra.lower())))
    linea = input()

ananagramas = []

for elemento in copia:
    if copia.count(elemento) == 1:
        ananagramas.append(lexico[copia.index(elemento)])

ananagramas.sort()

for ananagrama in ananagramas:
    print(ananagrama)