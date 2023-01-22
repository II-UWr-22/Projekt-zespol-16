import tkinter as tk
import random

# Globalne zmienne
panel = None
root = None
buttons = None
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

# Starting screen
def start_screen():
    root1 = tk.Tk()
    root1.geometry("300x200")
    root1.title("Super Saper")
    label1 = tk.Label(root1, text="Super Saper", font="Times 40 italic bold")
    label1.pack()
    button = tk.Button(root1, text=">START<", height=2, width=20,command=init_window)
    button.pack()
    ustawienia = tk.Button(root1, text=">USTAWIENIA<", height=2, width=20,command=size_settings)
    ustawienia.pack()
    zasady = tk.Button(root1, text=">JAK GRAĆ?<", height=2, width=20, command=zasadygry)
    zasady.pack()
    root1.resizable(False, False)
    root1.iconphoto(False, tk.PhotoImage(file='flaga.png'))
    return root1

def zasadygry():
    zasady = tk.Toplevel()
    zasady.geometry("600x75")
    zasady.title("Jak grać?")
    label = tk.Label(zasady, text="Gra polega na odkrywaniu na planszy poszczególnych pól w taki sposób, aby nie natrafić na minę.\n "
                                  "Na każdym z odkrytych pól napisana jest liczba min, \n"
                                  "które bezpośrednio stykają się z danym polem (od zera do ośmiu).\n"
                     "Źródło: https://pl.wikipedia.org/wiki/Saper_(gra_komputerowa)\n")
    label.pack()
    zasady.resizable(False, False)
    zasady.iconphoto(False, tk.PhotoImage(file='flaga.png'))


def set_size(x):
    global tbg, X, Y
    X = x
    Y = 2 * x
    size = f"{x} x {2 * x}"
    tbg.itemconfigure(1, text=size)


def set_time(x):
    global tbg, timer
    timer = x * 60
    tbg.itemconfigure(1, text=timer)


def size_settings():
    siz = tk.Toplevel()
    siz.geometry('420x280')
    siz.title("Size settings")
    top = tk.Frame(siz)
    top.pack(side=tk.TOP, pady=30)
    bottom = tk.Frame(siz)
    bottom.pack(side=tk.BOTTOM, pady=30)
    s1 = tk.Button(siz, text='size 1', command=lambda: set_size(15))
    s1.pack(in_=top, side=tk.LEFT, padx=25)
    s2 = tk.Button(siz, text='size 2', command=lambda: set_size(20))
    s2.pack(in_=top, side=tk.LEFT, padx=25)
    s3 = tk.Button(siz, text='size 3', command=lambda: set_size(25))
    s3.pack(in_=top, side=tk.LEFT, padx=25)
    q1 = tk.Button(siz, text='back', command=lambda: siz.destroy())
    q1.pack(in_=bottom, side=tk.LEFT, padx=5)
    q2 = tk.Button(siz, text='next', command=lambda: [siz.destroy(), time_settings()])
    q2.pack(in_=bottom, side=tk.LEFT, padx=5)
    global tbg
    tbg = tk.Canvas(siz, height=150, width=120, bg='white')
    tbg.pack(pady=0)
    tbg.create_text((60, 55), anchor='center', text="10 x 10", fill='black', font='Digital-7 20 bold')
    siz.mainloop()


def time_settings():
    tim = tk.Tk()
    tim.geometry('420x280')
    tim.title("Time settings")
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
    q1 = tk.Button(tim, text='back', command=lambda: size_settings())
    q1.pack(in_=bottom, side=tk.LEFT, padx=5)
    q2 = tk.Button(tim, text='ok', command=lambda: tim.destroy())
    q2.pack(in_=bottom, side=tk.LEFT, padx=5)
    global tbg
    tbg = tk.Canvas(tim, height=100, width=300, bg='black')
    tbg.pack(pady=10)
    tbg.create_text((150, 40), text=str(300), fill='aquamarine', font='Digital-7 20 bold')
    tim.mainloop()

# Inicjalizacja głownego okienka gry
def init_window():
    global root, panel, buttons
    root = tk.Toplevel()
    root.geometry("600x600")
    root.title("Super Saper")
    root.anchor(tk.CENTER)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (600 / 2))
    y_cordinate = int((screen_height / 2) - (600 / 2))
    root.geometry("{}x{}+{}+{}".format(600, 600, x_cordinate, y_cordinate))
    root.iconphoto(False, tk.PhotoImage(file='flaga.png'))
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
    buttons = [tk.Button(root, image=None, width=1, height=1) for i in range(X * Y)]
    for x in range(X):
        for y in range(Y):
            coordinate = y * X + x
            buttons[coordinate].grid(row=y + 1, column=x + 1)
            buttons[coordinate].bind('<Button-1>',
                                     lambda event, button=buttons[coordinate]: left_click_detonate(button, buttons))
            buttons[coordinate].bind('<Button-3>',
                                     lambda event, button=buttons[coordinate]: right_click_flag(button, panel))
    root.mainloop()

# Funkcja inicjalizująca panel do gry


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
    root1 = start_screen()
    root1.mainloop()
    
