# @Time    : 2018-09-15 22:39
# @Author  : DuQing
# @File    : maze_data.py
"""
description
"""
import numpy


class MazeData:
    def __init__(self, m, n):
        """
        :param m: 迷宫的宽
        :param n: 迷宫的高
        """
        self.__m = m
        self.__n = n
        self.rode = ' '
        self.wall = '#'
        self.entranceX = 1
        self.entranceY = 0
        self.exitX = m-2
        self.exitY = n-1
        self.maze = numpy.empty([m, n],numpy.string_)
        self.visited = numpy.zeros([m, n], dtype=bool)
        for i in range(m):
            for j in range(n):
                if i%2==1 and j%2==1:
                    self.maze[i][j] = self.rode
                else:
                    self.maze[i][j] = self.wall
        self.maze[self.entranceX][self.entranceY] = self.rode
        self.maze[self.exitX][self.exitY] = self.rode
        # print(self.maze)

    def in_area(self, x, y):
        return x>0 and y>0 and x<self.m and y<self.n

    @property
    def m(self):
        return self.__m

    @property
    def n(self):
        return self.__n

    @m.setter
    def m(self, value):
        self.__m = value

    @n.setter
    def n(self, value):
        self.__n = value

class Position:
    def __init__(self, x, y):
        self.x=x
        self.y=y

if __name__ == '__main__':
    m = MazeData(101, 101)
