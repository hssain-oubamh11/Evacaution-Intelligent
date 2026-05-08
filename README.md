Question 1

Pourquoi les coûts doivent-ils changer ?
Bonne réponse:
        Parce que :
        le bâtiment évolue,
        fumée et congestion changent,
        certains chemins deviennent dangereux.
Question 2

Pourquoi Bellman-Ford utilise "cout" ?
        le système ne cherche PAS la distance minimale,mais le risque minimale.

Question 3

        Pourquoi les couloirs sont des nœuds ?
        Parce que :
        ils représentent des zones critiques,
        fumée et congestion apparaissent dedans.
        
Question 4

Que représentent les arêtes ?
        Les connexions physiques :
        portes,
        passages,
        accès.
        
Question 5

        Pourquoi ajouter de la fumée augmente le coût ?
        Bonne réponse
        Parce que :
        le passage devient dangereux,
        Bellman-Ford doit l’éviter.
{{{{{
Le bâtiment est représenté sous forme de graphe pondéré.
Les nœuds représentent les espaces physiques du bâtiment.
Les arêtes représentent les connexions praticables entre ces espaces.
Les poids des arêtes sont dynamiques et dépendent du niveau de fumée, de congestion et du risque.
L’algorithme Bellman-Ford est utilisé pour trouver le chemin d’évacuation le plus sûr.”
}}}}}

