def osszegzo(lista):
    # osszesen = 0
    # for szam in lista:
    #     osszesen = osszesen + szam
    osszesen = sum(lista)
    print('A listában lévő számok összege: ', osszesen)


szamok = [3, 5, 19, 11, 17, 1]
osszegzo(szamok)
