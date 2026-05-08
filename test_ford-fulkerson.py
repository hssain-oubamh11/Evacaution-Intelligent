from batiment import creer_batiment

from ford_fulkerson import calculer_flux_maximal


# ==================================================
# CRÉATION DU BÂTIMENT
# ==================================================

G = creer_batiment()


# ==================================================
# CALCUL DU FLUX MAXIMAL
# ==================================================

flux, details = calculer_flux_maximal(
    G,
    source="A",
    sortie="Sortie2"
)


# ==================================================
# AFFICHAGE DES RÉSULTATS
# ==================================================

print("\n===== FLUX MAXIMAL =====")

print("Source : A")

print("Sortie : Sortie2")

print("Flux maximal :", flux)


print("\n===== DÉTAILS DES FLUX =====")

for noeud, destinations in details.items():

    print(f"\n{noeud} :")

    for destination, valeur in destinations.items():

        print(
            f"  -> {destination} : {valeur}"
        )