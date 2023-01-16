import tkinter as tk
import random
# Globalne zmienne
X = 30
Y = 15
bomb_count = 50
timer = 0
flags = bomb_count
detonated = 0
end = False


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
    przyciski = init_buttons(root)


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
    for y in range(Y):
        for x in range(X):
            coordinate = y * X + x
            buttons[coordinate].grid(row=y + 1, column=x + 1)
            buttons[coordinate].bind('<Button-3>', lambda event, button=buttons[coordinate]: right_click_flag(button, panel))
    return buttons


def init_preboard():
    pass


def init_board_of_bombs():
    board_of_bombs = []
    for y in range(Y):
        row = []
        for x in range(X):
            row.append(0)
        board_of_bombs.append(row)
    licznik_bomb = flags
    while licznik_bomb > 0:
        x = random.randint(0, X - 1)
        y = random.randint(0, Y - 1)
        if board_of_bombs[x][y] == 0:
            board_of_bombs[x][y] = 1
            licznik_bomb -= 1
    return board_of_bombs


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
    flaga = tk.PhotoImage(file='flaga.png')
    panel = init_panel(root)
    buttons = init_buttons(root)
    root.mainloop()
