from unittest import TestCase
from starmie import AStarProblem


class PathFinder(AStarProblem):

    def __init__(self, start, goal):
        assert isinstance(start, Vertex) and isinstance(goal, Vertex)
        self.start = start
        self.goal = goal

    def get_start(self):
        return self.start

    def is_goal(self, v):
        return v is self.goal

    def get_neighbors(self, v):
        return v.edges.keys()

    def get_path_cost(self, from_v, to_v):
        assert to_v in from_v.edges
        return from_v.edges[to_v].weight

    def estimate_heuristic_cost(self, v):
        x1, y1 = v.pos
        x2, y2 = self.goal.pos
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


class Vertex:

    def __init__(self, pos):
        assert len(pos) == 2
        self.pos = pos
        self.edges = {}

    def __repr__(self):
        return '<%s pos=%s>' % (type(self).__name__, self.pos)


class Edge:

    def __init__(self, v1, v2, weight):
        assert isinstance(v1, Vertex) and isinstance(v2, Vertex)
        v1.edges[v2] = self
        v2.edges[v1] = self
        self.weight = weight


class TestGraph(TestCase):

    def test_solve(self):
        v = [Vertex((0, 0)), Vertex((7, 0)), Vertex((5, 5)),
             Vertex((15, 6)), Vertex((10, 10)), Vertex((1, 8))]
        e = [Edge(v[0], v[1],  7), Edge(v[0], v[2],  9), Edge(v[0], v[5], 14),
             Edge(v[1], v[2], 10), Edge(v[1], v[3], 15), Edge(v[2], v[3], 11),
             Edge(v[2], v[5],  2), Edge(v[3], v[4],  6), Edge(v[4], v[5],  9)]
        actual = PathFinder(v[0], v[4]).solve()
        expected = [v[0], v[2], v[5], v[4]]
        self.assertEqual(expected, actual)
