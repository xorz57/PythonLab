import collections


class Graph:
    def __init__(self):
        self.edges = {}

    def bfs(self, start, finish):
        frontier = collections.deque()
        explored = {}
        path = []
        frontier.append(start)
        explored[start] = None
        while frontier:
            current = frontier.popleft()
            if current == finish:
                path.append(current)
                while explored[current]:
                    current = explored[current]
                    path.append(current)
                path.reverse()
                return path
            for neighbor in self.edges[current]:
                if neighbor not in explored:
                    frontier.append(neighbor)
                    explored[neighbor] = current
        return path

    def dfs(self, start, finish):
        frontier = collections.deque()
        explored = {}
        path = []
        frontier.append(start)
        explored[start] = None
        while frontier:
            current = frontier.pop()
            if current == finish:
                path.append(current)
                while explored[current]:
                    current = explored[current]
                    path.append(current)
                path.reverse()
                return path
            for neighbor in self.edges[current]:
                if neighbor not in explored:
                    frontier.append(neighbor)
                    explored[neighbor] = current
        return path
