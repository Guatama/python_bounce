from tkinter import *
from time import sleep

from game_elements import Ball, Platform, Score

def create_window():
    tk = Tk()
    tk.Title("Game - Snake")
    tk.resizable(0, 0)
    tk.wm_attributes('-topmost', 1)

    canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
    canvas.pack()

    tk.update()
    return tk


def main():
    pass


if __name__ == "__main__":
    main()
