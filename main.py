import matplotlib.pyplot as plt

from batiment import creer_batiment

from agents import creer_agents

from simulation import lancer_simulation

from evenements import (
    declencher_incendie,
    propager_fumee
)
from statistiques import (
    calculer_statistiques,
    afficher_statistiques
)

plt.ion()
# ==================================================
# CRÉATION DU BÂTIMENT
# ==================================================

G = creer_batiment()


# ==================================================
# ÉVÉNEMENTS
# ==================================================

declencher_incendie(
    G,
    "Couloir1",
    "Sortie1",
    intensite=5
)

propager_fumee(G)


# ==================================================
# CRÉATION DES AGENTS
# ==================================================

agents = creer_agents()


# ==================================================
# FENÊTRE GRAPHIQUE
# ==================================================

plt.figure(figsize=(10, 7))


# ==================================================
# LANCEMENT SIMULATION
# ==================================================

lancer_simulation(
    G,
    agents,
    iterations=6
)
# ==================================================
# STATISTIQUES
# ==================================================
""" stats = calculer_statistiques(
    agents,
    temps_total=6
)

afficher_statistiques(stats)"""


# ==================================================
# GARDER FENÊTRE OUVERTE
# ==================================================

plt.show()