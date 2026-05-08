
from config import ALPHA, BETA, GAMMA, DELTA


def calculer_cout(distance,
                   congestion,
                   fumee,
                   risque):

    cout = (
        ALPHA * distance +
        BETA * congestion +
        GAMMA * fumee +
        DELTA * risque
    )

    return round(cout, 2)


def mettre_a_jour_couts(G):

    for u, v, data in G.edges(data=True):

        distance = data["distance"]
        congestion = data["congestion"]
        fumee = data["fumee"]

        # -------------------------
        # Calcul du risque
        # -------------------------
        risque = fumee + congestion

        # -------------------------
        # Nouveau coût
        # -------------------------
        nouveau_cout = calculer_cout(
            distance,
            congestion,
            fumee,
            risque
        )

        # -------------------------
        # Mise à jour
        # -------------------------
        data["cout"] = nouveau_cout