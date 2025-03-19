from Pràctica_2.funcions import llegir_registre, get_num_monedes,escriure_registre, tira_ordinador_aleatori, tira_ordinador

num_partides = 1000
nom_file = 'registre'

for partida in range(num_partides):
    registre = llegir_registre(nom_file)
    monedes_restants = get_num_monedes(nom_file)
    guanyador = None
    aleatori_monedes_quedaven = None
    aleatori_monedes_tretes = None

    print(f'[ {monedes_restants} monedes ]')

    while monedes_restants > 0:

        monedes_restants, aleatori_monedes_quedaven, aleatori_monedes_tretes = tira_ordinador_aleatori(aleatori_monedes_quedaven, aleatori_monedes_tretes,monedes_restants, registre)
        print(f'[ {monedes_restants} monedes ]')

        if monedes_restants == 0:
            guanyador = 'ordinador aleatori'
            print(f'Ha guanyat l\'{guanyador}')
            if aleatori_monedes_quedaven:
                registre[aleatori_monedes_quedaven-1][aleatori_monedes_tretes-1] = 1
            break

        monedes_restants, aleatori_monedes_quedaven, aleatori_monedes_tretes = tira_ordinador(aleatori_monedes_quedaven, aleatori_monedes_tretes,monedes_restants, registre)
        print(f'[ {monedes_restants} monedes ]')
        
        if monedes_restants == 0:
            guanyador = 'ordinador'
            print(f'Ha guanyat l\'{guanyador}')
            if aleatori_monedes_quedaven:
                registre[aleatori_monedes_quedaven-1][aleatori_monedes_tretes-1] = 1
            break

    escriure_registre(nom_file,registre)