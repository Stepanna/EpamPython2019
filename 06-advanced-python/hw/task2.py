"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной

Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

"""
from queue import Queue


class Graph:
    def __init__(self, E):
        self.E = E

    def __iter__(self):
        first_ver = list(self.E.keys())[0]
        self.used = {}
        self.used[first_ver] = True
        self.queue = Queue()
        self.queue.put(first_ver)
        return self

    def __next__(self):
        while not self.queue.empty():
            vertice = self.queue.get()
            for neighbor in range(len(self.E[vertice])):
                neighbor_vert = self.E[vertice][neighbor]
                if neighbor_vert not in self.used.keys():
                    self.used[neighbor_vert] = True
                    self.queue.put(neighbor_vert)
            return vertice
        raise StopIteration


if __name__ == '__main__':
    E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
    graph = Graph(E)

    for vertice in graph:
        print(vertice)
