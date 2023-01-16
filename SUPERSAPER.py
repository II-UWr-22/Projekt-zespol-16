import tkinter as tk
import random
import sys
X = 30
Y = 15
# Globalne zmienne
bomb_counter = 50
timer = 0
flags = bomb_counter
detonated = 0
end = False


def init_window():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Super Saper")
    root.anchor(tk.CENTER)
    return root


def init_panel(root):
    bomb_counter = tk.Label(root, bg='black', fg='aquamarine', font=("Digital-7", 30))
    bomb_counter.grid(row=0, column=1, columnspan=7, ipadx=6, pady=25)
    bomb_counter['text'] = '0050'
    face = tk.Button(root, width=2)
    face.grid(row=0, column=(X//2)-1, columnspan=3, pady=25)
    clock = tk.Label(root,  bg='black', fg='aquamarine', font=("Digital-7", 30))
    clock.grid(row=0, column=X-6, columnspan=7, ipadx=6, pady=25)
    update_clock(root, clock)
    panel = [bomb_counter, face, clock]
    return panel


def update_clock(root, clock):
    global timer
    timer += 1
    if timer < 10:
        clock['text'] = "000" + str(timer)
    elif timer < 100:
        clock['text'] = "00" + str(timer)
    elif timer < 1000:
        clock['text'] = "0" + str(timer)
    else:
        clock['text'] = str(timer)
    root.after(1000, update_clock, root, clock)


def init_buttons(root):
    buttons = [tk.Button(root, width=2) for i in range(X*Y)]
    for y in range(Y):
        for x in range(X):
            buttons[y*X+x].grid(row=y+1, column=x+1)
    return buttons


def init_preboard():
    pass
    # randomizacja planszy


def init_board_of_bombs():
    board_of_bombs = []
    for y in range(Y):
        row = []
        for x in range(X):
            row.append(0)
        board_of_bombs.append(row)
    licznik_bomb = bomb_counter
    while licznik_bomb > 0:
        x = random.randint(0, X-1)
        y = random.randint(0, Y-1)
        if board_of_bombs[x][y] == 0:
            board_of_bombs[x][y] = 1
            licznik_bomb -= 1
    return board_of_bombs


if __name__ == "__main__":
    root = init_window()
    panel = init_panel(root)
    buttons = init_buttons(root)
    root.mainloop()
