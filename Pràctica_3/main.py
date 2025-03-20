from funcions import calcular_coincidencia

n_simulacions = 1000  # Nombre de simulacions per cada mida de grup
mida_minima_grup = 2 # Grup mínim de 2 persones
mida_maxima_grup = 100  # Grup màxim de 100 persones

probabilitats = []

for mida_grup in range(mida_minima_grup,mida_maxima_grup):
    nou_resultat = calcular_coincidencia(mida_grup, n_simulacions)
    probabilitats.append(nou_resultat)

# simular_probabilitat
# representar_resultats