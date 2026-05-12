import torch
from torch_geometric.nn import GCNConv
from torch_geometric.utils import from_networkx

import torch.nn.functional as F
from torch_geometric.nn import GCNConv

def convertir_graphe_pyg(G):
    # Convertir le graphe NetworkX en format PyTorch Geometric
    #convertir automatique
    data = from_networkx(G)
    return data

#création des features pour les noeuds
def creer_features_noeuds(G):
    features = []
    # Parcours des noeuds
    for noeud in G.nodes(data=True):
        nom = noeud[0]
        data = noeud[1]
        fumee = data["fumee"]
        temperature = data["temperature"]
        congestion = data["congestion"]
        danger = data["danger"]
        # Création du vecteur de caractéristiques pour ce noeud
        feature_vector = [
            fumee,
            temperature,
            congestion,
            danger
        ]
        features.append(feature_vector)
    x=torch.tensor(features, dtype=torch.float)
    return x
#Modèle GCN
class ModeleGCN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        #couche 1
        self.conv1 = GCNConv(
            in_channels=4,
            out_channels=8
        )
        #couche 2
        self.conv2 = GCNConv(
            in_channels=8,
            out_channels=1
        )
    def forward(self,x,edge_index):
        #couche 1
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        #couche 2
        x = self.conv2(x, edge_index)
        return x
    



