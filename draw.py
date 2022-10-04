from tkinter import *
from math import sin, cos, pi

SIZE = 600


def wave(img, amplitude):
    """Draw area bounded by cosinus and sinus waves"""
    for x in range(0, SIZE):
        y_cos = SIZE // 2 + amplitude * cos((4 * pi * x / SIZE))
        y_sin = SIZE // 2 + amplitude * sin((4 * pi * x / SIZE))
        for y in range(SIZE // 2 - amplitude, SIZE // 2 + amplitude):
            if y_cos < y_sin:
                if y_cos <= y <= y_sin:
                    img.put("red", (x, y))
            else:
                if y_sin <= y <= y_cos:
                    img.put("red", (x, y))


def main():
    """Create your image and call your functions inside this function."""
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#ffffff")
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")

    # Enter your drawing functions here
    wave(img, 100)

    mainloop()


if __name__ == '__main__':
    main()
