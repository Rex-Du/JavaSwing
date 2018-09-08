# @Time    : 2018-09-08 13:46
# @Author  : DuQing
# @File    : circle.py
"""
description
"""
import random
import time
from tkinter import Tk, Canvas, TclError


class Circle(object):
    def __init__(self, x, y, r, vx, vy):
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy


class AlgoFrame(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tk = Tk()
        self.tk.resizable(False, False)
        self.canvas = Canvas(self.tk, width=width, height=height)
        self.canvas.pack()

    def draw_circle(self, data_list):
        self.canvas.delete('all')
        for data in data_list:
            self.canvas.create_oval(data.x-data.r,data.y-data.r, data.x+data.r, data.y+data.r, fill='blue')
        self.tk.update()

    def run_circle(self, data_list):
        for data in data_list:
            if data.x<= data.r or data.x >=self.width-data.r:
                data.vx = -data.vx
            if data.y <=data.r or data.y >= self.height-data.r:
                data.vy = -data.vy
            data.x += data.vx
            data.y += data.vy
        # for i in range(len(data_list)):
        #     for j in range(i+1, len(data_list)):
        #         if (data_list[i].x - data_list[j].x)**2 + (data_list[i].y - data_list[j].y)**2 <= 4*r**2:
        #             data_list[i].vx = - data_list[i].vx
        #             data_list[i].vy = - data_list[i].vy
        #             data_list[j].vx = - data_list[j].vx
        #             data_list[j].vy = - data_list[j].vy





if __name__ == '__main__':
    frame_width = 1000
    frame_height = 700
    frame = AlgoFrame(frame_width, frame_height)
    r = 50
    circles_list = [Circle(random.randint(r,frame_width-r), random.randint(r, frame_height-r), r, random.randint(-8, 8), random.randint(-5, 5)) for i in range(10)]
    while True:
        try:
            frame.run_circle(circles_list)
            frame.draw_circle(circles_list)
            time.sleep(0.05)
        except TclError :
            break
