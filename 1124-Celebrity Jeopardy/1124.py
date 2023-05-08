while True:
    try:
        linea = input()
        print(linea)
    except EOFError:
        break