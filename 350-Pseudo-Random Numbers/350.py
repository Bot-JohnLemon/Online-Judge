numeros = input()
caso = 1
while numeros != '0 0 0 0':
    numeros = numeros.split(" ")
    z = int(numeros[0])
    i = int(numeros[1])
    m = int(numeros[2])
    l = int(numeros[3])

    n = (z * l + i) % m
    veces = 1
    nums = {l}

    while n not in nums:
        nums.add(n)
        n = (z * n + i) % m
        veces += 1

    if l == n:
        print(f"Case {caso}: {veces}")
    else:
        print(f"Case {caso}: {veces - 1}")
    caso += 1
    numeros = input()

