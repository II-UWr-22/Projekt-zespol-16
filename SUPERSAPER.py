import tkinter as tk
import random

# Globalne zmienne
clicks = 0
X = 30
Y = 15
bomb_count = 50
timer = 0
flags = bomb_count
detonated = 0
end = False
board_of_bombs = []
for i in range(X):
    row_of_bombs = []
    for j in range(Y):
        row_of_bombs.append(9)
    board_of_bombs.append(row_of_bombs)
clickable = []
for i in range(X):
    row_of_clicks = []
    for j in range(Y):
        row_of_clicks.append(1)
    clickable.append(row_of_clicks)

# Inicjalizacja głownego okienka gry
def init_window():
    root = tk.Tk()
    root.geometry("600x600")
    root.title("Super Saper")
    root.anchor(tk.CENTER)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (600 / 2))
    y_cordinate = int((screen_height / 2) - (600 / 2))
    root.geometry("{}x{}+{}+{}".format(600, 600, x_cordinate, y_cordinate))
    root.resizable(False, False)
    root.iconphoto(False, tk.PhotoImage(file='flaga.png'))
    return root


# Funkcja inicjalizująca panel do gry
def init_panel(root):
    flag = tk.Label(root, bg="black", fg="aquamarine", font=("Digital-7", 30))
    flag.grid(row=0, column=1, columnspan=7, ipadx=6, pady=25)
    update_flag_counter(root, flag)
    face = tk.Button(root, width=2, image=None)
    face.grid(row=0, column=(X // 2) - 1, columnspan=3, pady=25)
    face.bind('<Button-1>', lambda event: reset_game(root))
    clock = tk.Label(root, bg="black", fg="aquamarine", font=("Digital-7", 30))
    clock.grid(row=0, column=X - 6, columnspan=7, ipadx=6, pady=25)
    update_clock(root, clock)
    panel = [flag, face, clock]
    return panel


# Funkcja resetujące grę gdy kliknie się lewy przycisk myszy w buźkę
def reset_game(root):
    global timer
    timer = 0
    global flags
    flags = bomb_count
    global end
    end = False
    global clicks
    clicks = 0
    global board_of_bombs
    board_of_bombs = []
    for i in range(X):
        row_of_bombs = []
        for j in range(Y):
            row_of_bombs.append(9)
        board_of_bombs.append(row_of_bombs)
    global clickable
    clickable = []
    for i in range(X):
        row_of_clicks = []
        for j in range(Y):
            row_of_clicks.append(1)
        clickable.append(row_of_clicks)
    przyciski = init_buttons(root)
    update_flag_counter(root, panel[0])


# Funkcja licząca czas gry
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


# Funkcja licząca ilość pozostałych flag
def update_flag_counter(root, flag):
    global flags
    if flags < 0:
        flag['text'] = "0000"
    elif flags < 10:
        flag['text'] = "000" + str(flags)
    elif flags < 100:
        flag['text'] = "00" + str(flags)
    elif flags < 1000:
        flag['text'] = "0" + str(flags)


# Funkcja inicjalizująca guziki
def init_buttons(root):
    buttons = [tk.Button(root, image=None, width=1, height=1) for i in range(X * Y)]
    for x in range(X):
        for y in range(Y):
            coordinate = y * X + x
            buttons[coordinate].grid(row=y + 1, column=x + 1)
            buttons[coordinate].bind('<Button-1>', lambda event, button=buttons[coordinate]: left_click_detonate(button, buttons))
            buttons[coordinate].bind('<Button-3>', lambda event, button=buttons[coordinate]: right_click_flag(button, panel))
    return buttons


def init_board_of_bombs(button, buttons):
    global board_of_bombs
    index = buttons.index(button)
    dx = index % X
    dy = index // X
    for i in range(dx - 1, dx + 2):
        for j in range(dy - 1, dx + 2):
            if i >= 0 and i < X and j >= 0 and j < Y:
                board_of_bombs[i][j] = 0
    minescopy = bomb_count
    while minescopy > 0:
        randx = random.randint(0, X - 1)
        randy = random.randint(0, Y - 1)
        if board_of_bombs[randx][randy] == 9:
            board_of_bombs[randx][randy] = -1
            minescopy -= 1
    for i in range(X):
        for j in range(Y):
            if board_of_bombs[i][j] != -1:
                sasiedzi = 0
                for k in range(i - 1, i + 2):
                    for z in range(j - 1, j + 2):
                        if k >= 0 and k < X and z >= 0 and z < Y:
                            if board_of_bombs[k][z] == -1:
                                sasiedzi += 1
                board_of_bombs[i][j] = sasiedzi


def change(index, buttons, value):
    dx = index % X
    dy = index // X
    buttons[index].unbind('<Button-3>')
    buttons[index].unbind('<Button-1>')
    if value == 0:
        buttons[index] = tk.Label(root, bg ="bisque")
        buttons[index].grid(column=dx + 1, row=dy + 1)
    else:
        buttons[index] = tk.Label(root, text=str(value))
        buttons[index].grid(column=dx + 1, row=dy + 1)


def full(x, y, buttons):
    global board_of_bombs
    if board_of_bombs[x][y] == 0:
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i >= 0 and i < X and j >= 0 and j < Y:
                    if clickable[i][j] == 1:
                        indekz = j * X + i
                        change(indekz, buttons, board_of_bombs[i][j])
                        clickable[i][j] = 0
                        full(i, j, buttons)


def left_click_detonate(button, buttons):
    index = buttons.index(button)
    dy = index // X
    dx = index % X
    global clickable
    clickable[dx][dy] = 0
    global clicks
    if clicks == 0:
        init_board_of_bombs(button, buttons)
        clicks += 1
    value = board_of_bombs[dx][dy]
    if value == 0:
        full(dx, dy, buttons)
    if value == -1:
        exit(1)
    else:
        change(index, buttons, value)



# Funkcja flagująca (dodać obrazek!)
def right_click_flag(button, panel):
    global flags
    if button['text'] != "":
        button['text'] = ""
        flags += 1
    elif flags > 0:
        button['text'] = "F"
        flags -= 1
    update_flag_counter(root, panel[0])


# Główny loop gry
if __name__ == "__main__":
    root = init_window()
    panel = init_panel(root)
    buttons = init_buttons(root)
    root.mainloop()
    
