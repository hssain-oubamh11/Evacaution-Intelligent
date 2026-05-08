import networkx as nx


# ==================================================
# CALCUL DU FLUX MAXIMAL
# ==================================================

def calculer_flux_maximal(
        G,
        source,
        sortie):

    # --------------------------------------------------
    # Création graphe orienté
    # --------------------------------------------------

    G_flow = nx.DiGraph()

    # --------------------------------------------------
    # Copier les arêtes
    # avec leurs capacités
    # --------------------------------------------------

    for u, v, data in G.edges(data=True):

        capacite = data["capacite"]

        # Sens 1
        G_flow.add_edge(
            u,
            v,
            capacity=capacite
        )

        # Sens 2
        G_flow.add_edge(
            v,
            u,
            capacity=capacite
        )

    # --------------------------------------------------
    # Ford-Fulkerson
    # --------------------------------------------------

    flux_valeur, flux_dict = nx.maximum_flow(
        G_flow,
        source,
        sortie
    )

    return flux_valeur, flux_dict