from batiment import creer_batiment, afficher_batiment

from cout import mettre_a_jour_couts

from bellman_ford import trouver_chemin_sur


# ==================================================
# Création bâtiment
# ==================================================

G = creer_batiment()


# ==================================================
# Simulation danger
G["Couloir1"]["Sortie1"]["fumee"] = 5

G["A"]["Couloir1"]["congestion"] = 3


# ==================================================
# Mise à jour des coûts

mettre_a_jour_couts(G)


# ==================================================
# Recherche chemin sûr

resultat = trouver_chemin_sur(
    G,
    source="A",
    sorties=["Sortie1", "Sortie2"]
)


# ==================================================
# Résultat

print("\n===== CHEMIN LE PLUS SÛR =====")

print("Source :", resultat["source"])

print("Sortie choisie :", resultat["sortie"])

print("Chemin :", resultat["chemin"])

print("Coût total :", resultat["cout_total"])


# ==================================================
# Affichage

afficher_batiment(G)