import tkinter as tk
import random

X = 30
Y = 15
# Globalne zmienne
bomb_count = 50
timer = 0
flags = bomb_count
detonated = 0
end = False


def init_window():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Super Saper")
    root.anchor(tk.CENTER)
    root.resizable(False, False)
    root.iconphoto(False, tk.PhotoImage(file='flaga.png'))
    return root


def init_panel(root):
    bomb_counter = tk.Label(root, bg='black', fg='aquamarine', font=("Digital-7", 30))
    bomb_counter.grid(row=0, column=1, columnspan=7, ipadx=6, pady=25)
    update_bomb_counter(root, bomb_counter)
    face = tk.Button(root, width=2, image=None)
    face.grid(row=0, column=(X // 2) - 1, columnspan=3, pady=25)
    clock = tk.Label(root, bg='black', fg='aquamarine', font=("Digital-7", 30))
    clock.grid(row=0, column=X - 6, columnspan=7, ipadx=6, pady=25)
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


def update_bomb_counter(root, bomb_counter):
    global bomb_count
    if bomb_count < 0:
        bomb_counter['text'] = "0000"
    elif bomb_count < 10:
        bomb_counter['text'] = "000" + str(bomb_count)
    elif bomb_count < 100:
        bomb_counter['text'] = "00" + str(bomb_count)
    elif bomb_count < 1000:
        bomb_counter['text'] = "0" + str(bomb_count)
    root.after(2000, update_bomb_counter, root, bomb_counter)


def init_buttons(root):
    buttons = [tk.Button(root, image=None, width=1, height=1) for i in range(X * Y)]
    for y in range(Y):
        for x in range(X):
            coordinate = y * X + x
            buttons[coordinate].grid(row=y + 1, column=x + 1)
            buttons[coordinate].bind('<Button-3>', lambda event, button=buttons[coordinate]: right_click_flag(button, panel))
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
    licznik_bomb = bomb_count
    while licznik_bomb > 0:
        x = random.randint(0, X - 1)
        y = random.randint(0, Y - 1)
        if board_of_bombs[x][y] == 0:
            board_of_bombs[x][y] = 1
            licznik_bomb -= 1
    return board_of_bombs


# DO POPRAWY (FLAGOWANIE)
def right_click_flag(button, panel):
    global bomb_count
    bomb_count -= 1
    update_bomb_counter(root, panel[0])


if __name__ == "__main__":
    root = init_window()
    flaga = tk.PhotoImage(file='flaga.png')
    panel = init_panel(root)
    buttons = init_buttons(root)
    root.mainloop()
