import random

def jugar_partida(canvi):
    guanyador = random.randint(1,3)

    porta_triada = random.randint(1,3)

    porta_ensenyada = None

    guanya = False

    if guanyador == porta_triada:
        llista = [1, 2, 3]
        llista.remove(guanyador)
        porta_ensenyada = random.choice(llista)
        print(f'Oh! Has triat la porta {porta_triada}. Doncs t\'informo que la porta {porta_ensenyada} tenia una cabra!')

    elif guanyador != 1 and porta_triada != 1:
        print(f'Oh! Has triat la porta {porta_triada}. Doncs t\'informo que la porta 1 tenia una cabra!')
        porta_ensenyada = 1
    elif guanyador != 2 and porta_triada != 2:
        print(f'Oh! Has triat la porta {porta_triada}. Doncs t\'informo que la porta 2 tenia una cabra!')
        porta_ensenyada = 2
    else:
        print(f'Oh! Has triat la porta {porta_triada}. Doncs t\'informo que la porta 3 tenia una cabra!')
        porta_ensenyada = 3

    if canvi:
        llista = [1, 2, 3]
        llista.remove(porta_triada)
        llista.remove(porta_ensenyada)
        porta_triada = llista[0]
        print(f'Has canviat la porta, ara la que has triat és la {porta_triada}.')
    else:
        print(f'No has canviat la porta, la porta triada és la {porta_triada}.')


    if porta_triada == guanyador:
        guanya = True
        print('Felicitats! Has guanyat un cotxe!')
    else:
        print('Oooh! Has perdut...')

    return guanya
