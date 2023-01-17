# Le-Jeu-Puissance-4
#  [Notion!](https://scientific-viper-58f.notion.site/project-51175dd8d05f44e2be0831fefd381461)
### Résumé
La documentation suivante est pour une application qui met en œuvre un jeu de Puissance 4 en utilisant la bibliothèque Tkinter en Python.

L'application contient deux classes principales, **`CheckForWinner`** et **`Player`**. La classe **`CheckForWinner`** contient des fonctions qui vérifient s'il y a quatre éléments consécutifs horizontaux, verticaux ou diagonaux qui sont égaux dans le plateau de jeu représenté sous forme de matrice. La fonction **`search`** de cette classe prend une matrice en entrée et appelle les fonctions **`check_horizontal`**, **`check_vertical`** et **`check_diagonal`** pour vérifier s'il y a un gagnant dans le jeu. Chacune de ces fonctions renvoie une valeur booléenne indiquant s'il y a un gagnant ou non.

La classe **`Player`** est responsable de suivre le joueur actuel, elle est définie avec un compteur qui commence à 0 et si player est pair c'est le joueur 1 et s'il est impair c'est le joueur 2

La classe **`Board`** est responsable de créer le plateau de jeu sous forme de matrice de boutons à l'aide de la bibliothèque Tkinter. Elle a une fonction **`resetBord`** qui est utilisée pour réinitialiser le plateau de jeu à son état initial, et une fonction **`create_buttons`** qui crée les boutons pour le plateau de jeu. Lorsqu'un bouton est cliqué, le texte sur le bouton et la couleur du bouton changent pour indiquer le joueur actuel, et la fonction **`search`** de la classe **`CheckForWinner`** est appelée pour vérifier s'il y a un gagnant. S'il y a un gagnant, un message est affiché et le plateau de jeu est réinitialisé.

L'application utilise la bibliothèque Tkinter pour créer l'interface utilisateur graphique et la logique de jeu est implémentée dans les classes décrites ci-dessus.
