import random

# ==================================================
# DÉCLENCHEMENT D'INCENDIE

def declencher_incendie(
        G,
        u,
        v,
        intensite=5):

    # Ajouter fumée
    G[u][v]["fumee"] = intensite

    print(
        f"\n Incendie sur l'arête!!!! "
        f"{u} -> {v}"
    )


# ==================================================
# PROPAGATION DE LA FUMÉE
# ==================================================

def propager_fumee(G):
    nouvelles_fumees = []
    # Parcours arêtes
    for u, v, data in G.edges(data=True):
        fumee = data["fumee"]
        # Si fumée présente
        if fumee > 0:
            # Propagation voisins
            for voisin in G.neighbors(v):
                if voisin != u:
                    nouvelles_fumees.append((v, voisin))

    # --------------------------------------------------
    # Ajouter fumée
    # --------------------------------------------------

    for u, v in nouvelles_fumees:

        G[u][v]["fumee"] += 1

    print("\n Propagation de fumée")


# ==================================================
# BLOQUER UNE SORTIE
# ==================================================

def bloquer_sortie(
        G,
        sortie):

    # Trouver voisins sortie
    voisins = list(G.neighbors(sortie))

    for voisin in voisins:

        # Capacité = 0
        G[voisin][sortie]["capacite"] = 0

        # Très dangereux
        G[voisin][sortie]["fumee"] = 100

    print(
        f"\n Sortie bloquée : {sortie}"
    )