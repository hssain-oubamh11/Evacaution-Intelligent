import networkx as nx


def trouver_chemin_sur(
        G,
        source,
        sorties):

    meilleur_chemin = None

    cout_minimal = float("inf")

    meilleure_sortie = None
# --------------------------------------------------
    # Tester toutes les sorties
    
    for sortie in sorties:

        try:

            # ------------------------------------------
            # Bellman-Ford
            chemin = nx.bellman_ford_path(
                G,
                source=source,
                target=sortie,
                weight="cout"
            )

            # ------------------------------------------
            # Coût total du chemin
            cout_total = nx.path_weight(
                G,
                chemin,
                weight="cout"
            )

            # ------------------------------------------
            # Garder le meilleur

            if cout_total < cout_minimal:

                cout_minimal = cout_total

                meilleur_chemin = chemin

                meilleure_sortie = sortie

        except nx.NetworkXNoPath:

            continue

    return {
        "source": source,
        "sortie": meilleure_sortie,
        "chemin": meilleur_chemin,
        "cout_total": cout_minimal
    }