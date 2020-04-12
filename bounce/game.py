from tkinter import *
from time import sleep

from game_elements import Ball, Platform, Score


def create_window():
    tk = Tk()
    tk.title("Game - Snake")
    tk.resizable(0, 0)
    tk.wm_attributes('-topmost', 1)

    canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
    canvas.config(background="#272040")
    canvas.pack()

    tk.update()
    return tk, canvas


def main():
    tk, canvas = create_window()

    score = Score(canvas, 'green')
    paddle = Platform(canvas, 'White')
    ball = Ball(canvas, paddle, score, 'red')

    while not ball.hit_bottom:
        if paddle.started:
            ball.draw()
            paddle.draw()

        tk.update_idletasks()
        tk.update()
        sleep(0.01)

    sleep(3)


if __name__ == "__main__":
    main()
