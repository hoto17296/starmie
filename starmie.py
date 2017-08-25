from abc import ABCMeta, abstractmethod
import heapq


class AStarProblem(metaclass=ABCMeta):

    @abstractmethod
    def get_start(self):
        raise NotImplementedError()

    @abstractmethod
    def is_goal(self, node):
        raise NotImplementedError()

    @abstractmethod
    def get_neighbors(self, node):
        raise NotImplementedError()

    def get_path_cost(self, from_node, to_node):
        return 1

    def estimate_heuristic_cost(self, node):
        return 0

    def solve(self):
        # Initialize
        open_heap = []
        scored_nodes = {}

        # Set start node
        node = self.get_start()
        start = _ScoredNode(
            node=node,
            g=0,
            h=self.estimate_heuristic_cost(node),
            parent=None
        )
        scored_nodes[node] = start
        heapq.heappush(open_heap, start)

        # Search
        while True:
            # If open_heap is empty, return None as fail to find path
            if len(open_heap) == 0:
                return None
            # Take out node with the smallest score
            current = heapq.heappop(open_heap)
            # If the node is goal node, done search
            if self.is_goal(current.node):
                break
            # Search neighbor nodes
            for node in self.get_neighbors(current.node):
                neighbor = _ScoredNode(
                    node=node,
                    g=current.g + self.get_path_cost(current.node, node),
                    h=self.estimate_heuristic_cost(node),
                    parent=current
                )
                # If the node is already opened
                if node in scored_nodes:
                    old = scored_nodes[node]
                    new = neighbor
                    # Update node if the score improves
                    if new < old:
                        if old in open_heap:
                            open_heap.remove(old)
                        heapq.heappush(open_heap, new)
                        scored_nodes[node] = new
                else:
                    heapq.heappush(open_heap, neighbor)
                    scored_nodes[node] = neighbor

        # Generate path
        path = []
        while current is not None:
            path.append(current.node)
            current = current.parent

        return list(reversed(path))


class _ScoredNode:

    def __init__(self, node, g, h, parent):
        assert g >= 0 and h >= 0
        self.node = node
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def _val(self):
        return (self.f, self.g)

    def __lt__(self, node):
        return self._val() <  node._val()

    def __eq__(self, node):
        return self._val() == node._val()

    def __repr__(self):
        parent = None if self.parent is None else self.parent.node
        params = (type(self).__name__, self.node, self.g, self.h, self.f, parent)
        return '<%s node=%s g=%f h=%f f=%f parent=%s>' % params


__all__ = ['AStarProblem']
