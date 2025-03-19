def generar_aniversari():
    pass

def calcular_coincidencia(dimensio_grup, num_grups):
    num_coincidencia = 0

    for n in range(num_grups): # Fer-ho tantes vegades com grups tingui
        grup = []

        for m in range(dimensio_grup): # genero l'aniversari de totes les persones del grup
            grup.append(generar_aniversari())
            
        # mirar si hi ha dues persones amb el mateix dia d'aniversari