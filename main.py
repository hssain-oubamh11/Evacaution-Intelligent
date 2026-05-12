import matplotlib.pyplot as plt

from batiment import creer_batiment

from agents import creer_agents

from simulation import lancer_simulation

from ia.gnn import (
    convertir_graphe_pyg,
    creer_features_noeuds,
    ModeleGCN
)

from evenements import (
    declencher_incendie,
    propager_fumee
)
from statistiques import (
    calculer_statistiques,
    afficher_statistiques
)

plt.ion()
#==================================================
# CRÉATION DU Graphe (BÂTIMENT)
G = creer_batiment()   
print(G.nodes(data=True)) #pour afficher les noeuds et leurs attributs
#===========================
# CONVERSION GRAPHE POUR GNN
data = convertir_graphe_pyg(G)

# créer les features pour les noeuds
x=creer_features_noeuds(G)

#============================
#Modèle GCN
modele = ModeleGCN()
#============================
# prédiction 
prediction = modele(x,data.edge_index)
print(prediction)


# ==================================================
# ÉVÉNEMENTS

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

#plt.figure(figsize=(10, 7))


# ==================================================
# LANCEMENT SIMULATION
# ==================================================
""" lancer_simulation(
    G,
    agents,
    iterations=6
)
"""

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

#plt.show()