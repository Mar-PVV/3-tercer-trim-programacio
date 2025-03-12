import random
from Pràctica_2.funcions import llegir_registre, get_num_monedes,escriure_registre, tira_ordinador

nom_file = input('A quin joc vols jugar? Nom del registre: ')

registre = llegir_registre(nom_file)
monedes_restants = get_num_monedes(nom_file)
guanyador = None
aleatori_monedes_quedaven = None
aleatori_monedes_tretes = None

print(f'[ {monedes_restants} monedes ]')

while monedes_restants > 0:

    monedes_usuari = int(input(f'Queden {monedes_restants} monedes, quantes en vols treure? 1 o 2? '))
    
    while monedes_restants - monedes_usuari < 0 or monedes_usuari not in [1,2]:
        monedes_usuari = int(input(f'Torna a provar.'))

    monedes_restants -= monedes_usuari
    print(f'[ {monedes_restants} monedes ]')

    if monedes_restants == 0:
        guanyador = 'usuari'
        print(f'Ha guanyat l\'{guanyador}')
        if aleatori_monedes_quedaven:
            registre[aleatori_monedes_quedaven-1][aleatori_monedes_tretes-1] = 1
        break

    monedes_restants, aleatori_monedes_quedaven, aleatori_monedes_tretes = tira_ordinador(aleatori_monedes_quedaven, aleatori_monedes_tretes, monedes_restants, registre)

    print(f'[ {monedes_restants} monedes ]')
    
    if monedes_restants == 0:
        guanyador = 'ordinador'
        print(f'Ha guanyat l\'{guanyador}')
        break

escriure_registre(nom_file,registre)
print(registre)