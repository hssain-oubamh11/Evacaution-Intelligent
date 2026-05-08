
""""À chaque instant :

les agents bougent
les positions changent
les coûts évoluent
le graphe reste visible """
import matplotlib.pyplot as plt
import networkx as nx


# ==================================================
# AFFICHAGE DYNAMIQUE DE LA SIMULATION
# ==================================================

def afficher_simulation(G, agents):

    plt.clf()

    # --------------------------------------------------
    # Positions fixes du bâtiment
    # --------------------------------------------------

    pos = {

        "A": (0, 2),
        "B": (2, 2),

        "Couloir1": (1, 1),

        "C": (0, 0),
        "D": (2, 0),

        "Couloir2": (1, -1),

        "Sortie1": (3, 1),
        "Sortie2": (3, -1)
    }

    # --------------------------------------------------
    # Couleurs des noeuds
    # --------------------------------------------------

    couleurs_noeuds = []

    for noeud in G.nodes():

        if "Sortie" in noeud:

            couleurs_noeuds.append("lightgreen")

        elif "Couloir" in noeud:

            couleurs_noeuds.append("orange")

        else:

            couleurs_noeuds.append("skyblue")

    # --------------------------------------------------
    # Couleurs des arêtes selon fumée
    # --------------------------------------------------

    couleurs_aretes = []

    for u, v, data in G.edges(data=True):

        fumee = data["fumee"]

        if fumee >= 5:

            couleurs_aretes.append("red")

        elif fumee > 0:

            couleurs_aretes.append("orange")

        else:

            couleurs_aretes.append("black")

    # --------------------------------------------------
    # Dessin du graphe
    # --------------------------------------------------

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=couleurs_noeuds,
        edge_color=couleurs_aretes,
        width=3,
        node_size=2500,
        font_weight="bold"
    )

    # --------------------------------------------------
    # Affichage des coûts
    # --------------------------------------------------

    edge_labels = nx.get_edge_attributes(
        G,
        "cout"
    )

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_size=9
    )

    # --------------------------------------------------
    # Affichage des agents
    # --------------------------------------------------

    decalage = 0

    for agent in agents:

        x, y = pos[agent.position]

        # Décalage visuel
        x = x + (decalage * 0.08)
        y = y + (decalage * 0.08)

        # Agent
        plt.scatter(
            x,
            y,
            s=500,
            c="red",
            edgecolors="black"
        )

        # Texte agent
        plt.text(
            x,
            y + 0.12,
            f"P{agent.id}",
            fontsize=9,
            fontweight="bold"
        )

        decalage += 1

    # --------------------------------------------------
    # Titre
    # --------------------------------------------------

    plt.title(
        "Simulation d'évacuation intelligente",
        fontsize=15,
        fontweight="bold"
    )

    plt.axis("off")

    plt.pause(1.2)