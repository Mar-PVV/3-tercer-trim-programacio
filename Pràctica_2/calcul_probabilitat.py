from funcions import jugar_partida

num_partides = 20

guanyades_canvi = 0
guanyades_no_canvi = 0

for i in range(num_partides):
    # jugar partida canviant porta i emmagatzemar resultat
    jugar_partida(True)
    # jugar partida sense canviar de porta i emmagatzemar resultat
    jugar_partida(False)

# Fer histograma

# Calcular probabilitats i fer print