import tkinter

#Do usunięcia przy ostatecznej implementacji, chodzi po prostu o uruchomienie gry z time_chal = True
def play():
    global time_chal
    time_chal = True    #Chodzi o to, żeby timer chodził "do tyłu" przy tym ustawieniu a nie normalnie do przodu, wtedy starczy dodać jednego "if" do timera w grze i warunek zakończenia gry timer == 0
    

#Służy przede wszystkim do ustawienie zmiennej globalnej timer na odpowiedni czas. Poza tym służy do ustawienia czasu na timerze jako tekst na ekranie
def set_time(x):
    global tbg, timer
    timer = x * 60
    tbg.itemconfigure(1, text=timer)


#Analogicznie jak czas w funkcji set_time tylko dla rozmiaru
def set_size(x):
    global tbg, X, Y
    X = x
    Y = 2 * x
    size = f"{x} x {2 * x}"
    tbg.itemconfigure(1, text=size)


#Interfejs ustawień rozmiaru, otwiera się w osobnym oknie
def size_settings():
    siz = tkinter.Tk()
    siz.geometry('420x280')
    siz.title("Size settings")
    top = tkinter.Frame(siz)
    top.pack(side=tkinter.TOP, pady=30)
    bottom = tkinter.Frame(siz)
    bottom.pack(side=tkinter.BOTTOM, pady=30)
    s1 = tkinter.Button(siz, text='size 1', command=lambda: set_size(15))
    s1.pack(in_=top, side=tkinter.LEFT, padx=25)
    s2 = tkinter.Button(siz, text='size 2', command=lambda: set_size(20))
    s2.pack(in_=top, side=tkinter.LEFT, padx=25)
    s3 = tkinter.Button(siz, text='size 3', command=lambda: set_size(25))
    s3.pack(in_=top, side=tkinter.LEFT, padx=25)
    q1 = tkinter.Button(siz, text='back', command=lambda: siz.destroy())
    q1.pack(in_=bottom, side=tkinter.LEFT, padx=5)
    q2 = tkinter.Button(siz, text='next', command=lambda: [siz.destroy(), time_settings()])
    q2.pack(in_=bottom, side=tkinter.LEFT, padx=5)
    global tbg
    tbg = tkinter.Canvas(siz, height=150, width=120, bg='white')
    tbg.pack(pady=0)
    tbg.create_text((60, 55), anchor='center', text="10 x 10", fill='black', font='Digital-7 20 bold')
    siz.mainloop()


#Interfejs ustawień czasu, otwiera się w osobnym oknie
def time_settings():
    tim = tkinter.Tk()
    tim.geometry('420x280')
    tim.title("Time settings")
    top = tkinter.Frame(tim)
    top.pack(side=tkinter.TOP, pady=30)
    bottom = tkinter.Frame(tim)
    bottom.pack(side=tkinter.BOTTOM, pady=30)
    t1 = tkinter.Button(tim, text='1 minute', command=lambda: set_time(1))
    t1.pack(in_=top, side=tkinter.LEFT, padx=5)
    t3 = tkinter.Button(tim, text='3 minutes', command=lambda: set_time(3))
    t3.pack(in_=top, side=tkinter.LEFT, padx=5)
    t5 = tkinter.Button(tim, text='5 minutes', command=lambda: set_time(5))
    t5.pack(in_=top, side=tkinter.LEFT, padx=5)
    t10 = tkinter.Button(tim, text='10 minutes', command=lambda: set_time(10))
    t10.pack(in_=top, side=tkinter.LEFT, padx=5)
    t15 = tkinter.Button(tim, text='15 minutes', command=lambda: set_time(15))
    t15.pack(in_=top, side=tkinter.LEFT, padx=5)
    q1 = tkinter.Button(tim, text='back', command=lambda: size_settings())
    q1.pack(in_=bottom, side=tkinter.LEFT, padx=5)
    q2 = tkinter.Button(tim, text='ok', command=lambda: tim.destroy())
    q2.pack(in_=bottom, side=tkinter.LEFT, padx=5)
    global tbg
    tbg = tkinter.Canvas(tim, height=100, width=300, bg='black')
    tbg.pack(pady=10)
    tbg.create_text((150, 40), text=str(300), fill='aquamarine', font='Digital-7 20 bold')
    tim.mainloop()


#Główne menu wyzwań czasowych, to powinno się otwierać po przejściu ze starting screen
menu = tkinter.Tk()
menu.geometry('280x280')
menu.title("Time challenge")
top = tkinter.Frame(menu)
top.pack(side=tkinter.TOP, pady=30)
bottom = tkinter.Frame(menu)
bottom.pack(side=tkinter.BOTTOM, pady=30)
b1 = tkinter.Button(menu, text='back', command=lambda: menu.destroy())
b1.pack(in_=bottom, pady=5)
b2 = tkinter.Button(menu, text='settings', command=lambda: size_settings())
b2.pack(in_=bottom, pady=5)
b3 = tkinter.Button(menu, text='play', command=lambda: [play(), menu.destroy()])
b3.pack(in_=bottom, pady=5)
tbg = tkinter.Canvas(menu, height=100, width=300)
tbg.pack(pady=5)
tbg.create_text((140, 20), text="Time challenge", fill='black', font='Digital-7 20 bold')
menu.mainloop()
