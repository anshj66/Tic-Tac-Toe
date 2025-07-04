import tkinter as tk
from tkinter import messagebox
def chec_winner():
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]].cget('text') == buttons[combo[1]].cget('text') == buttons[combo[2]].cget('text') != '':
            buttons[combo[0]].config(bg='green')
            buttons[combo[1]].config(bg='green')
            buttons[combo[2]].config(bg='green')
            messagebox.showinfo("Winner", f"{buttons[combo[0]].cget('text')} wins!")
            root.quit()
def button_click(index):
    if buttons[index].cget('text') == '' and not winner:
        buttons[index].config(text=current_player)
        chec_winner()
        toggle_player()

def toggle_player():
    global current_player
    current_player = 'X' if current_player == 'O' else 'O'
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

current_player = 'X'
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()