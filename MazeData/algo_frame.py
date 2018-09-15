# @Time    : 2018-09-15 23:04
# @Author  : DuQing
# @File    : algo_frame.py
"""
description
"""
from tkinter import Tk, Canvas
from MazeData.maze_data import MazeData


class AlgoFrame:
    def __init__(self, maze_data, width, height):
        self.__maze_data = maze_data
        self.width = width
        self.height = height
        self.tk = Tk()
        self.tk.resizable(False, False)
        self.canvas = Canvas(self.tk, width=width, height=height)
        self.canvas.pack()

    def render(self):
        self.repaint()

    def repaint(self):
        w = self.width/self.__maze_data.n
        h = self.height/self.__maze_data.m

        for i in range(self.__maze_data.m):
            for j in range(self.__maze_data.n):
                if self.__maze_data.maze[i][j] == b' ':
                    self.canvas.create_rectangle(j*w,i*h, (j+1)*w, (i+1)*h, fill='white', outline = 'white')
                else:
                    self.canvas.create_rectangle(j * w, i * h, (j + 1) * w, (i + 1) * h, fill='blue', outline='blue')
        self.tk.update()

    def show(self):
        self.tk.mainloop()


if __name__ == '__main__':
    d = MazeData(101, 101)
    frame = AlgoFrame(d, 800, 600)
    frame.render()
    frame.show()



