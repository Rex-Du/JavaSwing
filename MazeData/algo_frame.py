# @Time    : 2018-09-15 23:04
# @Author  : DuQing
# @File    : algo_frame.py
"""
description
"""
from tkinter import Tk, Canvas
from MazeData.maze_data import MazeData


class AlgoFrame:
    def __init__(self, maze_data, m, n):
        self.maze_data = maze_data
        self.m=m
        self.n=n
        self.size = 5
        self.width = n*self.size
        self.height = m*self.size
        self.tk = Tk()
        self.tk.resizable(False, False)
        self.canvas = Canvas(self.tk, width=self.width, height=self.height, bg='blue')
        self.canvas.pack()

    def render(self):
        self.repaint()

    def repaint(self):
        self.canvas.delete('all')
        for i in range(self.m):
            for j in range(self.n):
                if self.maze_data.maze[i][j] == b' ' :
                    self.canvas.create_rectangle(j*self.size,i*self.size, (j+1)*self.size, (i+1)*self.size, fill='white', width=0)
                # else:
                #     self.canvas.create_rectangle(j * w, i * h, (j + 1) * w, (i + 1) * h, fill='blue', outline='blue')
        self.tk.update()

    def paint_point(self,x, y):
        if self.maze_data.maze[x][y] == b' ' :
            self.canvas.create_rectangle(y*self.size,x*self.size, (y+1)*self.size, (x+1)*self.size, fill='white', outline = 'white', width=1)
        self.tk.update()

    def show(self):
        self.tk.mainloop()


if __name__ == '__main__':
    d = MazeData(101, 101)
    frame = AlgoFrame(d, 800, 600)
    frame.render()
    frame.show()



