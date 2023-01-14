import tkinter as tk
import random
import sys
X = 20
Y = 30


def init_window():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Super Saper")
    return root


def init_panel(root):
    bomb_counter = tk.Label(root)
    bomb_counter.grid(row=0, column=0)
    bomb_counter['text'] = '0050'
    face = tk.Button(root)
    face.grid(row=0, column=X//2)
    clock = tk.Label(root)
    clock.grid(row=0, column=Y-10)
    clock['text'] = '0000'
    panel = [bomb_counter, face, clock]
    return panel

if __name__ == "__main__":
    root = init_window()
    panel = init_panel(root)
    root.mainloop()
