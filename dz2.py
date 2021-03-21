n = int(input())
if n >= 1:
    lista = input().split()
    jednocifren = broj = izbacen = 0
    maxbroj = -1
    for i in range(len(lista)):
        lista[i] = int(lista[i])
        if lista[i] >= 0 and lista[i] <= 9:
            jednocifren += 1
    if jednocifren == len(lista):
        temp1 = lista.copy()
        for i in range(len(lista)):
            temp1.pop(i)
            for j in range(len(temp1)):
                broj += temp1[j] * 10 ** (len(temp1) - 1 - j)
            if broj % (2 ** n) == 0 and broj > maxbroj:
                izbacen = i
                maxbroj = broj
            temp1 = lista.copy()
            broj = 0
        if len(lista) > 0 and maxbroj != -1:
            lista.pop(izbacen)
            print(lista)
        else:
            print([])