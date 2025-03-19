import csv, random

def llegir_registre(nom_file):
    registre = []
    with open(f'./Pràctica_5/registres/{nom_file}.csv','r') as f:
        reader = csv.reader(f)
        for index, row in enumerate(reader):
            if index > 0:
                registre.append([int(row[1]),int(row[2])])
    return registre

def escriure_registre(nom_file, registre):
    with open(f'./Pràctica_5/registres/{nom_file}.csv','w', newline='') as f:
        csv_writer = csv.writer(f, delimiter=',')
        fila = ['num_monedes','treure1','treure2']
        csv_writer.writerow(fila)
        for index, row in enumerate(registre):
            fila = [index+1,row[0],row[1]]
            csv_writer.writerow(fila)

def crear_registre(nom_file, num_monedes):
    registre = []

    # Crear taula de 0 de registre.
    for i in range(num_monedes):
        registre.append([0,0])
    
    escriure_registre(nom_file, registre)

def get_num_monedes(nom_file):
    registre = llegir_registre(nom_file)
    return len(registre)

def tira_ordinador(aleatori_monedes_quedaven, aleatori_monedes_tretes, monedes_restants, registre):
    
    treure_1 = registre[monedes_restants-1][0]
    treure_2 = registre[monedes_restants-1][1]

    if (treure_1 == 1 and treure_2 == 0) and monedes_restants > 1:
        monedes_restants -= 2
        print('L\'ordinador treu 2 monedes.')
    elif (treure_1 == 0 and treure_2 == 1) or monedes_restants == 1:
        monedes_restants -= 1
        print('L\'ordinador treu 1 moneda.')
    else:
        monedes_ordinador = random.randint(1,2)

        aleatori_monedes_quedaven = monedes_restants
        aleatori_monedes_tretes = monedes_ordinador

        monedes_restants -= monedes_ordinador
        print(f'L\'ordinador treu {monedes_ordinador} monedes (aleatori).')

    return monedes_restants, aleatori_monedes_quedaven, aleatori_monedes_tretes

def tira_ordinador_aleatori(aleatori_monedes_quedaven, aleatori_monedes_tretes, monedes_restants, registre):
    treure_1 = registre[monedes_restants-1][0]
    treure_2 = registre[monedes_restants-1][1]

    monedes_ordinador = random.randint(1,2)

    aleatori_monedes_quedaven = monedes_restants
    aleatori_monedes_tretes = monedes_ordinador

    monedes_restants -= monedes_ordinador
    print(f'L\'ordinador aleatori treu {monedes_ordinador} monedes (aleatori).')

    return monedes_restants, aleatori_monedes_quedaven, aleatori_monedes_tretes