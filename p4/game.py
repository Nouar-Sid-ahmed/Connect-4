import display
import constantes


# Function for create array (plateau)
def create_tab_game():

    tab = []

    for k in range(constantes.plateau_height):
        tab.append([])

        for i in range(constantes.plateau_width):
            tab[k].append(constantes.separator_row)

    return tab


# Function for test end of the game
def end_test(joueur, plateau):

    for i in range(0, 6):
        for j in range(0, 7):
            if i < 3 and plateau[i][j] == joueur and plateau[i+1][j] == joueur and plateau[i+2][j] == joueur and plateau[i+3][j] == joueur:
                return joueur
            elif j < 4 and plateau[i][j] == joueur and plateau[i][j+1] == joueur and plateau[i][j+2] == joueur and plateau[i][j+3] == joueur:
                return joueur
            elif i < 3 and j < 4 and plateau[i][j] == joueur and plateau[i+1][j+1] == joueur and plateau[i+2][j+2] == joueur and plateau[i+3][j+3] == joueur:
                return joueur
            elif i < 3 and j > 2 and plateau[i][j] == joueur and plateau[i+1][j-1] == joueur and plateau[i+2][j-2] == joueur and plateau[i+3][j-3] == joueur:
                return joueur
            
    compteur = 0

    for i in range(0, 6):
        for j in range(0, 7):
            if plateau[i][j] != '-':
                compteur += 1
            else:
                compteur = 0

    if compteur == 42:
        return True

    return False


# Function for interact with the players
def jouer(joueur, plateau):

    token_placed = False

    while not token_placed:

        y = input("Entrez l'abscisse compris entre 0 et " + str(constantes.plateau_width) + " : ")

        if y == "1" or y == "2" or y == "3" or y == "4" or y == "5" or y == "6" or y == "7":
            y = int(y)

            for r in range(constantes.plateau_height-1, -1, -1):
                if plateau[r][y - 1] == '-' and not token_placed:
                    plateau[r][y - 1] = joueur
                    token_placed = True

        if not token_placed:
            print(constantes.error_value)


# Function for start and manage the current game
def jeu(plateau):

    display.display_tab(plateau)
    bool_fin_jeu = False

    while not bool_fin_jeu:

        jouer(constantes.token_j1, plateau)
        display.display_tab(plateau)
        result_end_game = end_test(constantes.token_j1, plateau)

        if result_end_game == constantes.token_j1:
            print("Joueur 1 a gagné (token: " + constantes.token_j1 + ")")
            return 0

        elif result_end_game:
            print(constantes.player_score_equal)
            return 0

        jouer(constantes.token_j2, plateau)
        display.display_tab(plateau)
        result_end_game = end_test(constantes.token_j2, plateau)

        if result_end_game:
            print("Joueur 2 a gagné (token: " + constantes.token_j2 + ")")
            return 0

        elif result_end_game:
            print(constantes.player_score_equal)
            return 0
