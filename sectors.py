import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Carreguem l'arxiu de dades des del fitxer CSV
data = pd.read_csv("brecha_salarial_europa.csv")

# Extreu les columnes dels sectors
sectors = data.columns.values[4:]

# Filtra les dades per a Espanya
sp = data.loc[data["Country"] == "Spain"]

# Selecciona només les columnes dels sectors
sp = sp[sectors]

# Obté els anys únics
anys = data["Year"].unique()

# Calcula la mitjana i la desviació estàndard
mitj = sp.mean(axis=1)
desv = sp.std(axis=1)

# Crea diccionaris amb els anys com a claus i mitjana/desviació com a valors
dic1 = {anys[i]: mitj.tolist()[i] for i in range(len(anys))}
dic2 = {anys[i]: desv.tolist()[i] for i in range(len(anys))}

print("La mitjana per any de tots els sectors a Espanya és", dic1)
print("La desviació per year de tots els sectors a Espanya és", dic2)

# Crea el gràfic de la bretxa salarial
plt.figure(figsize=(15, 5))  # Canviat la mida del gràfic principal
plt.plot(anys, mitj.tolist())
plt.fill_between(anys, mitj + desv, mitj - desv, alpha=0.5, linewidth=0)
plt.axis([2010, 2021, -4, 25])
plt.axhline(y=0, color='r', linestyle='-')
plt.xlabel("Anys")
plt.ylabel("Mitjana dels sectors")
plt.title("Bretxa salarial a Espanya (2010-2021)")
plt.grid(True)

# Especifica la ruta completa per desar el gràfic principal
save_path_main = r"C:\Users\sergi\Documents\IT Academy projects\Python\bretxa.png"

# Desa el gràfic principal a la ruta especificada
plt.savefig(save_path_main)

# Opcionalment, obre la imatge desada amb un visualitzador d'imatges
import subprocess
subprocess.Popen([save_path_main], shell=True)

# Crea una gràfica tipus subplot amb 10 columnes i 2 files de mida 30x10
fig, axs = plt.subplots(nrows=2, ncols=10, figsize=(30, 10))

# Fem un bucle per a les taules
for ax, sector in zip(axs.flat, sectors):
    ax.bar(anys, sp[sector])

    # Fiquem el títol del sector com a títol de la taula
    ax.set_title(str(sector))

# Especifica la ruta completa per desar el gràfic de les taules
save_path_taules = r"C:\Users\sergi\Documents\IT Academy projects\Python\taules.png"

# Desa el gràfic de les taules a la ruta especificada
plt.savefig(save_path_taules)

# Opcionalment, obre la imatge desada amb un visualitzador d'imatges
subprocess.Popen([save_path_taules], shell=True)

# Realitza l'anàlisi de regressió per al sector "water supply"
aigua = sp[sectors[5]].tolist()
fig, ax = plt.subplots()
ax.scatter(anys, aigua)
stats_result = stats.linregress(anys, aigua)
ax.plot(anys, anys * stats_result[0] + stats_result[1])
ax.set_title("Regressió lineal del sector " + str(sectors[5]))
print("El pendent és ", stats_result[0], "per hi ha un descens significatiu de la bretxa salarial al llarg dels anys")
print("El punt d'intersecció és ", stats_result[1], "que marca quan la línia creurà l'eix x, per tant a partir de 2022 no hauria d'haver bretxa salarial")
print("El coeficient de Pearson és", stats_result[2], "és força proper a -1, per tant hi ha una correlació negativa gairebé perfecta entre els valors de la bretxa i els anys")
print("El p-value és", stats_result[3], " i per obtenir rellevància estadística hauria de ser menor que 0.05. Potser afecta que la mostra feta servir és més aviat reduïda")
print("Ha estat un bon fitting, ja que visualment la línia i els punts es mostren propers. Seria un mal fitting si la línia estigues molt allunyada dels punts (underfitting) o els recorregués exactament (overfitting)")

# Especifica la ruta completa per desar el gràfic del sector "water supply"
save_path_water_supply = r"C:\Users\sergi\Documents\IT Academy projects\Python\water_supply.png"

# Desa el gràfic del sector "water supply" a la ruta especificada
plt.savefig(save_path_water_supply)

# Opcionalment, obre la imatge desada amb un visualitzador d'imatges
subprocess.Popen([save_path_water_supply], shell=True)

# Mostra el gràfic (si és necessari)
# plt.show()
