from bellman_ford import trouver_chemin_sur
from agents import deplacer_agent
import time
from cout import mettre_a_jour_couts
from visualisation import afficher_simulation # Optionnel : pour visualiser la simulation
import time
# ==================================================
# CALCUL DES CHEMINS
# ==================
def calculer_chemins_agents(G, agents):

    sorties = ["Sortie1", "Sortie2"]

    for agent in agents:

        if agent.evacue:
            continue

        resultat = trouver_chemin_sur(
            G,
            source=agent.position,
            sorties=sorties
        )

        agent.chemin = resultat["chemin"]

        agent.index_chemin = 0


# ==================================================
# DÉPLACEMENT DES AGENTS
# ==================================================

def deplacer_tous_agents(agents):

    for agent in agents:

        deplacer_agent(agent)


# ==================================================
# AFFICHAGE CONSOLE
# ==================================================

def afficher_etat_agents(agents):

    print("\n===== ÉTAT DES AGENTS =====")

    for agent in agents:

        print(
            f"Agent {agent.id}"
            f" | Position : {agent.position}"
            f" | Evacué : {agent.evacue}"
        )


# ==================================================
# SIMULATION PRINCIPALE
# ==================================================

def lancer_simulation(
        G,
        agents,
        iterations=5):

    plt_active = False

    for t in range(iterations):

        print("\n")
        print("=" * 50)

        print(f"TEMPS {t}")

        print("=" * 50)

        # ---------------------------------------------
        # Mise à jour des coûts
        # ---------------------------------------------

        mettre_a_jour_couts(G)

        # ---------------------------------------------
        # Recalcul chemins
        # ---------------------------------------------

        calculer_chemins_agents(G, agents)

        # ---------------------------------------------
        # Déplacement agents
        # ---------------------------------------------

        deplacer_tous_agents(agents)

        # ---------------------------------------------
        # Affichage terminal
        # ---------------------------------------------

        afficher_etat_agents(agents)

        # ---------------------------------------------
        # Affichage graphique
        # ---------------------------------------------

        afficher_simulation(G, agents)

        # ---------------------------------------------
        # Pause
        # ---------------------------------------------

        time.sleep(1)