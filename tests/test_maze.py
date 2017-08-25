from unittest import TestCase
from starmie import AStarProblem


class Maze(AStarProblem):
    WALL = 'O'
    START = 'S'
    GOAL = 'G'
    ROAD = ' '
    PATH = '*'

    def __init__(self, map_data, allow_slant=True):
        self.map = []
        self.start = None
        self.goal = None
        for x, line in enumerate(map_data):
            self.map.append([])
            for y, char in enumerate(line):
                assert char in (self.WALL, self.START, self.GOAL, self.ROAD)
                self.map[x].append(char)
                if char == self.START: self.start = (x, y)
                if char == self.GOAL: self.goal = (x, y)
        self.shape = (len(self.map), len(self.map[0]))
        self.move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        if allow_slant:
            self.move += [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    def get_start(self):
        return self.start

    def is_goal(self, node):
        return node == self.goal

    def get_neighbors(self, node):
        x, y = node
        w, h = self.shape
        neighbors = [(x + dx, y + dy) for dx, dy in self.move]
        neighbors = filter(lambda pos: 0 <= pos[0] < w and 0 <= pos[1] < h, neighbors)
        neighbors = filter(lambda pos: self.map[pos[0]][pos[1]] != self.WALL, neighbors)
        return neighbors

    def get_path_cost(self, from_node, to_node):
        dx = from_node[0] - to_node[0]
        dy = from_node[1] - to_node[1]
        return (dx ** 2 + dy ** 2) ** 0.5

    def estimate_heuristic_cost(self, node):
        x1, y1 = node
        x2, y2 = self.goal
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def solve(self):
        path = super().solve()
        path_str = ''
        for x, line in enumerate(self.map):
            for y, char in enumerate(line):
                if (x, y) in path and char == self.ROAD:
                    path_str += self.PATH
                else:
                    path_str += char
            path_str += '\n'
        return path_str


class TestMaze(TestCase):

    def test_solve(self):
        map_data = [
            'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO',
            'OS  O     O     O         O          O',
            'O   O  O  O  O  O         O    OOOO GO',
            'O      O     O  O   OOOO  O    O  OOOO',
            'OOOOOOOOOOOO OOOOO  O     O    O     O',
            'O                O  O     O          O',
            'O        OOO     O  O     OOOOOOOOO  O',
            'O  OO    O    OOOO  O     O      OO  O',
            'O   O    O          O     O  O   O   O',
            'O   OOO  O          O        O   O   O',
            'O        O          O        O       O',
            'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO',
        ]
        actual = Maze(map_data).solve()
        expected = '\n'.join([
            'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO',
            'OS* O  ** O     O         O    ***** O',
            'O  *O *O *O  O  O   ****  O   *OOOO GO',
            'O   ** O  ** O  O  *OOOO* O   *O  OOOO',
            'OOOOOOOOOOOO*OOOOO *O    *O   *O     O',
            'O            *   O *O    *O    ****  O',
            'O        OOO *   O *O    *OOOOOOOOO* O',
            'O  OO    O   *OOOO* O    *O ***  OO* O',
            'O   O    O    ****  O    *O* O * O*  O',
            'O   OOO  O          O     *  O  *O*  O',
            'O        O          O        O   *   O',
            'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO',
            '',
        ])
        self.assertEqual(expected, actual)
