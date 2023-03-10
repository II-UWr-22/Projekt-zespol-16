import tkinter as tk
from tkinter import *
import random

# Globalne zmienne
panel = None
root = None
buttons = None
clicks = 0
X = 30
Y = 15
bomb_count = (X * Y) // 10
win_count = 0
timer = 0
time_limit = 9999
flags = bomb_count
toplev = 0
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


# Starting screen
def start_screen():
    root1 = tk.Tk()
    root1.geometry("300x200")
    root1.title("Super Saper")
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (300 / 2))
    y_cordinate = int((screen_height / 2) - (200 / 2))
    root1.geometry("{}x{}+{}+{}".format(300, 200, x_cordinate, y_cordinate))
    label1 = tk.Label(root1, text="Super Saper", font="Times 40 italic bold")
    label1.pack()
    button = tk.Button(root1, text=">START<", height=2, width=20, command=init_window)
    button.pack()
    ustawienia = tk.Button(root1, text=">USTAWIENIA<", height=2, width=20, command=size_settings)
    ustawienia.pack()
    zasady = tk.Button(root1, text=">JAK GRAĆ?<", height=2, width=20, command=zasadygry)
    zasady.pack()
    root1.resizable(False, False)
    root1.iconphoto(False, tk.PhotoImage(file='Grafika\\flaga.png'))
    return root1


def zasadygry():
    zasady = tk.Toplevel()
    zasady.geometry("600x75")
    screen_width = zasady.winfo_screenwidth()
    screen_height = zasady.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (600 / 2))
    y_cordinate = int((screen_height / 2) - (75 / 2))
    zasady.geometry("{}x{}+{}+{}".format(600, 75, x_cordinate, y_cordinate))
    zasady.title("Jak grać?")
    label = tk.Label(zasady,
                     text="Gra polega na odkrywaniu na planszy poszczególnych pól w taki sposób, aby nie natrafić na minę.\n "
                          "Na każdym z odkrytych pól napisana jest liczba min, \n"
                          "które bezpośrednio stykają się z danym polem (od zera do ośmiu).\n"
                          "Źródło: https://pl.wikipedia.org/wiki/Saper_(gra_komputerowa)\n")
    label.pack()
    zasady.resizable(False, False)
    zasady.iconphoto(False, tk.PhotoImage(file='Grafika\\znakzapytania.png'))
    zasady.mainloop()


def set_size(x):
    global tbg, X, Y, bomb_count
    X = x
    Y = x // 2
    bomb_count = (X * Y) // 10
    size = f"{x} x {x // 2}"
    tbg.itemconfigure(1, text=size)


def set_time(x):
    global tbg, time_limit
    time_limit = x * 60
    tbg.itemconfigure(1, text=str(time_limit)+'s')


def size_settings():
    siz = tk.Toplevel()
    siz.geometry('420x280')
    siz.title("Size settings")
    screen_width = siz.winfo_screenwidth()
    screen_height = siz.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (420 / 2))
    y_cordinate = int((screen_height / 2) - (280 / 2))
    siz.geometry("{}x{}+{}+{}".format(420, 280, x_cordinate, y_cordinate))
    top = tk.Frame(siz)
    top.pack(side=tk.TOP, pady=30)
    bottom = tk.Frame(siz)
    bottom.pack(side=tk.BOTTOM, pady=30)
    s1 = tk.Button(siz, text='Easy', command=lambda: set_size(20))
    s1.pack(in_=top, side=tk.LEFT, padx=25)
    s2 = tk.Button(siz, text='Medium', command=lambda: set_size(30))
    s2.pack(in_=top, side=tk.LEFT, padx=25)
    s3 = tk.Button(siz, text='Hard', command=lambda: set_size(40))
    s3.pack(in_=top, side=tk.LEFT, padx=25)
    q1 = tk.Button(siz, text='back', command=lambda: siz.destroy())
    q1.pack(in_=bottom, side=tk.LEFT, padx=5)
    q2 = tk.Button(siz, text='next', command=lambda: [siz.destroy(), time_settings()])
    q2.pack(in_=bottom, side=tk.LEFT, padx=5)
    global tbg
    tbg = tk.Canvas(siz, height=150, width=120, bg='white')
    tbg.pack(pady=0)
    tbg.create_text((60, 55), anchor='center', text="20 x 10", fill='black', font='Digital-7 20 bold')
    siz.iconphoto(False, zebatka)
    siz.mainloop()


def time_settings():
    tim = tk.Tk()
    tim.geometry('420x280')
    tim.title("Time settings")
    tim.anchor(tk.CENTER)
    screen_width = tim.winfo_screenwidth()
    screen_height = tim.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (420 / 2))
    y_cordinate = int((screen_height / 2) - (280 / 2))
    tim.geometry("{}x{}+{}+{}".format(420, 280, x_cordinate, y_cordinate))
    top = tk.Frame(tim)
    top.pack(side=tk.TOP, pady=30)
    bottom = tk.Frame(tim)
    bottom.pack(side=tk.BOTTOM, pady=30)
    t1 = tk.Button(tim, text='1 minute', command=lambda: set_time(1))
    t1.pack(in_=top, side=tk.LEFT, padx=5)
    t3 = tk.Button(tim, text='3 minutes', command=lambda: set_time(3))
    t3.pack(in_=top, side=tk.LEFT, padx=5)
    t5 = tk.Button(tim, text='5 minutes', command=lambda: set_time(5))
    t5.pack(in_=top, side=tk.LEFT, padx=5)
    t10 = tk.Button(tim, text='10 minutes', command=lambda: set_time(10))
    t10.pack(in_=top, side=tk.LEFT, padx=5)
    t15 = tk.Button(tim, text='15 minutes', command=lambda: set_time(15))
    t15.pack(in_=top, side=tk.LEFT, padx=5)
    q1 = tk.Button(tim, text='back', command=lambda: [tim.destroy(), size_settings()])
    q1.pack(in_=bottom, side=tk.LEFT, padx=5)
    q2 = tk.Button(tim, text='ok', command=lambda: tim.destroy())
    q2.pack(in_=bottom, side=tk.LEFT, padx=5)
    global tbg
    tbg = tk.Canvas(tim, height=100, width=300, bg='white')
    tbg.pack(pady=10)
    tbg.create_text((150, 40), text=str(300)+'s', font='Digital-7 20 bold')
    tim.mainloop()


# Inicjalizacja głownego okienka gry
def init_window():
    global root, panel, buttons, toplev
    root = tk.Toplevel(bg="azure3")
    root.geometry(str(X * 25) + 'x' + str(X * 20))
    root.title("Super Saper")
    root.anchor(tk.CENTER)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (X * 25 / 2))
    y_cordinate = int((screen_height / 2) - (X * 20 / 2))
    root.geometry("{}x{}+{}+{}".format(X * 25, X * 20, x_cordinate, y_cordinate))
    root.iconphoto(False, tk.PhotoImage(file='Grafika\\bomba.png'))
    flag = tk.Label(root, bg="black", fg="aquamarine", font=("Digital-7", 30))
    flag.grid(row=0, column=1, columnspan=6, ipadx=7, pady=35)
    update_flag_counter(root, flag)
    face = tk.Button(root, image=zdjecie)
    face.grid(row=0, column=(X // 2) - 1, columnspan=3, pady=35)
    face.bind('<Button-1>', lambda event: reset_game(root))
    clock = tk.Label(root, bg="black", fg="aquamarine", font=("Digital-7", 30))
    clock.grid(row=0, column=X - 5, columnspan=6, ipadx=7, pady=35)
    update_clock(root, clock)
    panel = [flag, face, clock]
    buttons = [tk.Button(root, image=None, width=1, height=1) for i in range(X * Y)]
    for x in range(X):
        for y in range(Y):
            coordinate = y * X + x
            buttons[coordinate].grid(row=y + 1, column=x + 1)
            buttons[coordinate].bind('<Button-1>',
                                     lambda event, button=buttons[coordinate]: left_click_detonate(button, buttons))
            buttons[coordinate].bind('<Button-3>',
                                     lambda event, button=buttons[coordinate]: right_click_flag(button, panel))
    reset_game(root)
    toplev = root
    root.mainloop()


# Funkcja resetujące grę gdy kliknie się lewy przycisk myszy w buźkę
def reset_game(root):
    global timer
    timer = 0
    global flags
    flags = bomb_count
    global clicks
    clicks = 0
    global win_count
    win_count = 0
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
    global timer, end, time_limit
    timer += 1
    if timer >= time_limit:
        timer = 0
        losink = tk.Toplevel()
        losink.geometry("400x50")
        screen_width = losink.winfo_screenwidth()
        screen_height = losink.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (400 / 2))
        y_cordinate = int((screen_height / 2) - (50 / 2))
        losink.geometry("{}x{}+{}+{}".format(400, 50, x_cordinate, y_cordinate))
        losink.resizable(False, False)
        przegranak = tk.Label(losink, text="Przegrałeś!!!\n"
                                          "Spróbuj ponowanie klikając START.", font="Times 18 italic bold")
        przegranak.pack()
        losink.after(5000, lambda: losink.destroy())
        toplev.destroy()
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
    else:
        flag['text'] = "9999"


# Funkcja inicjalizująca guziki
def init_buttons(root):
    buttons = [tk.Button(root, fg='red', width=1, height=1) for i in range(X * Y)]
    for x in range(X):
        for y in range(Y):
            coordinate = y * X + x
            buttons[coordinate].grid(row=y + 1, column=x + 1)
            buttons[coordinate].bind('<Button-1>',
                                     lambda event, button=buttons[coordinate]: left_click_detonate(button, buttons))
            buttons[coordinate].bind('<Button-3>',
                                     lambda event, button=buttons[coordinate]: right_click_flag(button, panel))
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


def change(index, buttons, value, button):
    global flags, winn, win_count
    dx = index % X
    dy = index // X
    buttons[index].unbind('<Button-3>')
    buttons[index].unbind('<Button-1>')
    if value != -1:
        win_count += 1
    if value == 0:
        buttons[index].configure(bg="bisque")
        buttons[index] = tk.Label(root, bg="bisque")
        buttons[index].grid(column=dx + 1, row=dy + 1)
    else:
        buttons[index] = tk.Label(root, text=str(value), fg=number_colors(value))
        buttons[index].grid(column=dx + 1, row=dy + 1)


def number_colors(value):
    if value == 1: return "blue4"
    if value == 2: return "green4"
    if value == 3: return "sienna4"
    if value == 4: return "Hotpink2"
    if value == 5: return "turquoise1"
    if value == 6: return "darkorchid"
    if value == 7: return "orange"
    if value == 8: return "dark khaki"


def full(x, y, buttons, button):
    global board_of_bombs, flags, win_count
    if board_of_bombs[x][y] == 0:
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i >= 0 and i < X and j >= 0 and j < Y:
                    if clickable[i][j] == 1:
                        indekz = j * X + i
                        value = board_of_bombs[i][j]
                        if buttons[indekz]['text'] == "F":
                            flags += 1
                            flag = panel[0]
                            update_flag_counter(root, flag)
                        change(indekz, buttons, board_of_bombs[i][j], button)
                        clickable[i][j] = 0
                        full(i, j, buttons, button)


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
        full(dx, dy, buttons, button)
    if value == -1:
        losing = tk.Toplevel()
        losing.geometry("400x50")
        screen_width = losing.winfo_screenwidth()
        screen_height = losing.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (400 / 2))
        y_cordinate = int((screen_height / 2) - (50 / 2))
        losing.geometry("{}x{}+{}+{}".format(400, 50, x_cordinate, y_cordinate))
        losing.resizable(False, False)
        przegrana = tk.Label(losing, text="Przegrałeś!!!\n"
                                          "Spróbuj ponowanie klikając START.", font="Times 18 italic bold")
        przegrana.pack()
        losing.after(5000, lambda: losing.destroy())
        toplev.destroy()
    else:
        change(index, buttons, value, button)
    if win_count == X*Y - bomb_count:
        winning = tk.Toplevel()
        winning.geometry("400x70")
        screen_width = winning.winfo_screenwidth()
        screen_height = winning.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (400 / 2))
        y_cordinate = int((screen_height / 2) - (70 / 2))
        winning.geometry("{}x{}+{}+{}".format(400, 70, x_cordinate, y_cordinate))
        winning.resizable(False, False)
        winnek = tk.Label(winning, text="Wygrałeś!!! Gratulacje!!\n"
                                        "Zagraj ponowanie klikając START.", font="Times 18 italic bold")
        winnek.pack()
        winning.after(5000, lambda: winning.destroy())
        toplev.destroy()


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
    root1 = start_screen()
    zebatka = tk.PhotoImage(file='Grafika\\zebatka.png')
    zdjecie = tk.PhotoImage(file="Grafika\\buzka2.png")
    root1.mainloop()
