from funcions import jugar_partida

num_partides = 20

guanyades_canvi = 0
guanyades_no_canvi = 0

dades = []

for i in range(num_partides):
    # jugar partida canviant porta i emmagatzemar resultat
    resultat = jugar_partida(True)
    if resultat:
        guanyades_canvi += 1
        dades.append('canvi')
        
    # jugar partida sense canviar de porta i emmagatzemar resultat
    resultat = jugar_partida(False)
    if resultat:
        guanyades_no_canvi += 1
        dades.append('no_canvi')

# Fer histograma
plt.hist(dades, bins=2, color='skyblue', edgecolor='black')
plt.show()

# Calcular probabilitats i fer print

print('S\'han jugat un total de '+str(2*num_partides)+' partides.')

total_partides_guanyades = guanyades_canvi+guanyades_no_canvi
print(f'D\'aquestes se\'n han guanyat {total_partides_guanyades}.' )

prob_guanya_si_canvi = guanyades_canvi / (guanyades_canvi+guanyades_no_canvi)
prob_guanya_no_canvi = guanyades_no_canvi / (guanyades_canvi+guanyades_no_canvi)

labels = 'canvi', 'no_canvi'
sizes = [prob_guanya_si_canvi,prob_guanya_no_canvi]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()
