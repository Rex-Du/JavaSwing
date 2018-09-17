# @Time    : 2018-09-17 21:50
# @Author  : DuQing
# @File    : algo_control.py
"""
description
"""
import random

from MazeData.algo_frame import AlgoFrame
from MazeData.maze_data import MazeData, Position
from collections import deque

class AlgoControl:
    def __init__(self, m, n):
        self.maze_data = MazeData(m, n)
        self.frame = AlgoFrame(self.maze_data, m, n)
        self.derection = [[0, -1], [1, 0],[0, 1], [-1, 0]]

    def repaint(self):
        self.frame.repaint()
        self.frame.show()

    def gen_maze(self, x, y):
        self.frame.paint_point(self.maze_data.entranceX, self.maze_data.entranceY)
        que = deque()

        que.append(Position(x, y))
        self.frame.paint_point(x, y)
        self.maze_data.visited[x][y] = True
        while True:
            r = random.randint(0, 1)
            try:
                if r:
                    curr = que.pop()
                else:
                    curr = que.popleft()
            except Exception:
                break

            for i in range(4):
                new_x = curr.x + self.derection[i][0] *2
                new_y = curr.y + self.derection[i][1] *2
                if self.maze_data.in_area(new_x, new_y) and not self.maze_data.visited[new_x][new_y]:
                    self.maze_data.maze[curr.x+self.derection[i][0]][curr.y+self.derection[i][1]] = self.maze_data.rode
                    self.frame.paint_point(curr.x+self.derection[i][0], curr.y+self.derection[i][1])
                    r = random.randint(0, 1)
                    if r:
                        que.append(Position(new_x, new_y))
                    else:
                        que.appendleft(Position(new_x, new_y))
                    self.maze_data.visited[new_x][new_y] = True
                    self.frame.paint_point(new_x, new_y)
            # self.frame.repaint()
        self.frame.paint_point(self.maze_data.exitX, self.maze_data.exitY)
        self.frame.show()

if __name__ == '__main__':
    maze = AlgoControl(129, 299)
    maze.gen_maze(1, 1)

