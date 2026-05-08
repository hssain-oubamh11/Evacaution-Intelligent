# ==================================================
# CLASSE AGENT
# ==================================================

class Agent:

    def __init__(self, agent_id, position):

        self.id = agent_id

        self.position = position

        self.evacue = False

        self.chemin = []

        self.index_chemin = 0


# ==================================================
# CRÉATION DES AGENTS
# ==================================================

def creer_agents():

    agents = []

    agents.append(Agent(1, "A"))
    agents.append(Agent(2, "A"))

    agents.append(Agent(3, "B"))

    agents.append(Agent(4, "C"))

    agents.append(Agent(5, "D"))

    return agents


# ==================================================
# DÉPLACEMENT D'UN AGENT
# ==================================================

def deplacer_agent(agent):

    # Déjà évacué
    if agent.evacue:
        return

    # Pas de chemin
    if not agent.chemin:
        return

    # Déplacement
    if agent.index_chemin < len(agent.chemin) - 1:

        agent.index_chemin += 1

        nouvelle_position = agent.chemin[
            agent.index_chemin
        ]

        agent.position = nouvelle_position

        # Vérifier sortie
        if "Sortie" in nouvelle_position:

            agent.evacue = True