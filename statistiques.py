# ==================================================
# STATISTIQUES DE LA SIMULATION
# ==================================================

def calculer_statistiques(
        agents,
        temps_total):

    total_agents = len(agents)

    evacues = 0

    non_evacues = 0

    # --------------------------------------------------
    # Comptage agents
    # --------------------------------------------------

    for agent in agents:

        if agent.evacue:

            evacues += 1

        else:

            non_evacues += 1

    # --------------------------------------------------
    # Pourcentage évacuation
    # --------------------------------------------------

    taux_evacuation = (
        evacues / total_agents
    ) * 100

    # --------------------------------------------------
    # Résultats
    # --------------------------------------------------

    stats = {

        "total_agents": total_agents,

        "evacues": evacues,

        "non_evacues": non_evacues,

        "taux_evacuation": taux_evacuation,

        "temps_total": temps_total
    }

    return stats


# ==================================================
# AFFICHAGE DES STATISTIQUES
# ==================================================

def afficher_statistiques(stats):

    print("\n")
    print("=" * 50)

    print("STATISTIQUES FINALES")

    print("=" * 50)

    print(
        f"Nombre total d'agents : "
        f"{stats['total_agents']}"
    )

    print(
        f"Agents évacués : "
        f"{stats['evacues']}"
    )

    print(
        f"Agents non évacués : "
        f"{stats['non_evacues']}"
    )

    print(
        f"Taux d'évacuation : "
        f"{stats['taux_evacuation']:.2f}%"
    )

    print(
        f"Temps total simulation : "
        f"{stats['temps_total']}"
    )