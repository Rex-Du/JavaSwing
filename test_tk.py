# @Time    : 2018-09-06 22:24
# @Author  : DuQing
# @File    : test_tk.py
"""
description
"""
import random
import time
from tkinter import Tk, Canvas


def draw(canvas, width, height, money):
    money.sort()
    w = width // len(money)
    canvas.delete('all')
    for index, value in enumerate(money):
        if value >= 0:
            canvas.create_rectangle(index * w + 2, height / 2 - value, index * w + w - 2, height / 2,
                                    fill='blue')
        else:
            canvas.create_rectangle(index * w + 2, height / 2, index * w + w - 2, height / 2 - value,
                                    fill='red')



def random_put_get(money):
    for i in range(len(money)):
        money[i] -= 1
        x = random.randint(0, 99)
        money[x] += 1
    return money


def main():
    tk = Tk()
    tk.resizable(False, False)
    canvas = Canvas(tk, width=1000, height=800)
    # canvas.create_rectangle(10,10, 200,200)
    # print(canvas.winfo_width())
    # print(canvas.winfo_height())
    canvas.pack()
    money = [100 for i in range(100)]
    while True:
        try:
            for i in range(100):
                money = random_put_get(money)
            draw(canvas, 1000, 800, money)
            tk.update()
            time.sleep(0.03)
        except Exception as e:
            break
    # tk.mainloop()


if __name__ == '__main__':
    main()
