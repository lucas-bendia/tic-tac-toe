from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Initialisation des variables globales
Player1 = 'X'
stop_game = False

# Fonction qui est appelée lorsque l'utilisateur clique sur un bouton
def clicked(r,c):
	global Player1
	# Si le joueur est "X", le bouton est marqué "X" et le tour passe à "O"
	if Player1 == "X" and states[r][c] == 0 and stop_game == False:
		b[r][c].configure(text = "X", fg = "white", bg = "red")
		states[r][c] = 'X'
		Player1='O'
	# Si le joueur est "O", le bouton est marqué "O" et le tour passe à "X"
	if Player1 == 'O' and states[r][c] == 0 and stop_game == False:
		b[r][c].configure(text = 'O', fg = "white", bg = "blue")
		states[r][c] = "O"
		Player1 = "X"
	# Vérifie si le jeu est terminé après chaque coup
	check_if_win()

# Fonction qui vérifie si le jeu est terminé
def check_if_win():
	global stop_game
	# Vérifie les lignes, les colonnes et les diagonales pour voir si une victoire a eu lieu
	for i in range(3):
		if states[i][0] == states[i][1] == states[i][2] !=0:
			stop_game = True
			messagebox.showinfo("Winner !", states[i][0] + " Win !")
			break
		elif states [0][i] == states[1][i] == states[2][i] != 0:
			stop_game = True
			messagebox.showinfo("Winner !", states[0][i]+ " Win !")
			break
		elif states[0][0] == states[1][1] == states[2][2] !=0:
			stop_game = True
			messagebox.showinfo("Winner !", states[0][0]+ " Win !")
			break
		elif states[0][2] == states[1][1] == states[2][0] !=0:
			stop_game = True
			messagebox.showinfo("Winner !" , states[0][2]+ " Win !")
			break
		# Vérifie si tous les boutons ont été cliqués et qu'il n'y a pas de gagnant (match nul)
		elif all(states[i][j] != 0 for i in range(3) for j in range(3)):
			stop_game = True
			messagebox.showinfo("Draw", "Draw")

# Création de la fenêtre de jeu
root = Tk()
root.title("GeeksForGeeks-:Tic Tac Toe")
root.resizable(0,0)
root.configure(bg='black')

# Initialisation des boutons et des états
b = [[0,0,0] for _ in range(3)]
states = [[0,0,0] for _ in range(3)]

# Création des boutons et ajout à la grille
for i in range(3):
	for j in range(3):
		b[i][j] = Button(height = 4, width = 8, font = ("Helvetica","20"), command = lambda r = i, c = j : clicked(r,c))
		b[i][j].grid(row = i, column = j)

mainloop()
