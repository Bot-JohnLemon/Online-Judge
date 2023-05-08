lineas = []
while True:
    try:
        lineas.append(input().split())
    except:
        break

for linea in lineas:
    n = int(linea[0])
    sec = linea[1:]

    restas = []
    for i in range(n - 1):
        restas.append(abs(int(sec[i]) - int(sec[i + 1])))

    if n == 1:
        print("Jolly")
    elif len(set(restas)) != n - 1:
        print("Not jolly")
    elif min(restas) == 1 and max(restas) == n - 1:
        print("Jolly")
    else:
        print("Not jolly")
    