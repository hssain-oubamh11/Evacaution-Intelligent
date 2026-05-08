import networkx as nx
import matplotlib.pyplot as plt
def creer_batiment():
    G = nx.Graph()

    # -------------------------
    # Ajout des salles
    # -------------------------
    salles = [
        "A", "B", "C", "D",
        "Couloir1", "Couloir2",
        "Sortie1", "Sortie2"
    ]

    G.add_nodes_from(salles)

    # -------------------------
    # Ajout des connexions
    # -------------------------
    connexions = [
        ("A", "Couloir1"),
        ("B", "Couloir1"),
        ("C", "Couloir2"),
        ("D", "Couloir2"),

        ("Couloir1", "Couloir2"),

        ("Couloir1", "Sortie1"),
        ("Couloir2", "Sortie2")
    ]

    # distance = poids initial
    for u, v in connexions:
        G.add_edge(
            u,
            v,
            distance=1,
            fumee=0,
            congestion=0,
            capacite=10,
            cout=1
        )

    return G
G=creer_batiment()
def afficher_batiment(G):

    plt.figure(figsize=(10, 7))

    # -------------------------
    # Position manuelle
    # -------------------------
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

    # -------------------------
    # Types de noeuds
    # -------------------------
    salles = ["A", "B", "C", "D"]
    couloirs = ["Couloir1", "Couloir2"]
    sorties = ["Sortie1", "Sortie2"]

    # -------------------------
    # Dessin des salles
    # -------------------------
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=salles,
        node_color="skyblue",
        node_size=2500,
        label="Salles"
    )

    # -------------------------
    # Dessin des couloirs
    # -------------------------
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=couloirs,
        node_color="orange",
        node_size=3000,
        label="Couloirs"
    )

    # -------------------------
    # Dessin des sorties
    # -------------------------
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=sorties,
        node_color="lightgreen",
        node_size=3000,
        label="Sorties"
    )

    # -------------------------
    # Arêtes
    # -------------------------
    nx.draw_networkx_edges(
        G,
        pos,
        width=2
    )

    # -------------------------
    # Labels noeuds
    # -------------------------
    nx.draw_networkx_labels(
        G,
        pos,
        font_size=11,
        font_weight="bold"
    )

    # -------------------------
    # Labels des coûts
    # -------------------------
    edge_labels = nx.get_edge_attributes(G, "cout")

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_size=10
    )

    # -------------------------
    # Mise en forme
    # -------------------------
    plt.title(
        "Modélisation du bâtiment sous forme de graphe",
        fontsize=15,
        fontweight="bold"
    )

    plt.legend(scatterpoints=1)
    plt.axis("off")
    plt.show()
from cout import mettre_a_jour_couts


# ==========================================
# TEST FUMÉE / CONGESTION
# ==========================================

G["Couloir1"]["Sortie1"]["fumee"] = 5

G["A"]["Couloir1"]["congestion"] = 3

mettre_a_jour_couts(G)

afficher_batiment(G)
afficher_batiment(G)