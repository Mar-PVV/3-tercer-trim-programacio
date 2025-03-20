import random

def generar_aniversari():
    mes = random.randint(1,12)

    if mes == 2:
        dia = random.randint(1,28)
    elif mes in [4, 6, 9, 11]:
        dia = random.randint(1,30)
    else:
        dia = random.randint(1,31)
    return f'{dia}-{mes}'

def calcular_coincidencia(dimensio_grup, num_simulacions):
    num_coincidencia = 0

    for n in range(num_simulacions): # Fer-ho tantes vegades com grups tingui
        grup = []

        for m in range(dimensio_grup): # genero l'aniversari de totes les persones del grup
            grup.append(generar_aniversari())

        for aniversari in grup:
            if grup.count(aniversari) > 1:
                num_coincidencia += 1
                break

    return num_coincidencia/num_simulacions        
