import constantes


# Function for display array on the terminal (display plateau)
def display_tab(plateau):

    for i in range(0, constantes.plateau_height):
        for j in range(0, constantes.plateau_width):
            print(constantes.separator_col, end="")
            print(plateau[i][j], end="")

        print(constantes.separator_col)

    print(constantes.separator_tab)
