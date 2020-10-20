"""
Given a Directed Graph and two vertices in it, check whether there is a path from the first given vertex to
the second
"""


class Vertex:
    def __init__(self, vertex):
        self.adjacent_to = []
        self.vertex = vertex
        self.seen = False


def find_path(graph, v1, v2):

    queue = []

    queue.append(graph[v1]) # enqueue the first vertex
    graph[v1].seen = True

    while len(queue) > 0: # while the queue is not empty

        curr = queue.pop(0) # dequeue an element (implement w/o list bec this is an O(n) operation)

        for item in curr.adjacent_to: # enqueue neighbors
            if item == v2: # if neighbors is v2 then path exists
                return True
            graph[item].seen = True
            queue.append(graph[item])

    return False


""" Example One """

v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)

v1.adjacent_to.append(2)
v1.adjacent_to.append(3)
v3.adjacent_to.append(2)
v3.adjacent_to.append(4)
v4.adjacent_to.append(3)

graph = {1 : v1, 2 : v2, 3 : v3, 4 : v4}

# print(find_path(graph, 1, 5))

""" Example Two """

v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)
v6 = Vertex(6)

v1.adjacent_to.append(2)
v2.adjacent_to.append(3)
v4.adjacent_to.append(3)
v4.adjacent_to.append(5)
v5.adjacent_to.append(2)
v5.adjacent_to.append(1)
v6.adjacent_to.append(4)

graph1 = {1 : v1, 2 : v2, 3 : v3, 4 : v4, 5 : v5, 6 : v6}

# print(find_path(graph1, 2, 1))

""" Example Three """

v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)

v1.adjacent_to.append(1)
v1.adjacent_to.append(2)
v1.adjacent_to.append(4)
v2.adjacent_to.append(1)
v2.adjacent_to.append(3)
v2.adjacent_to.append(4)
v3.adjacent_to.append(4)
v4.adjacent_to.append(5)

graph2 = {1 : v1, 2 : v2, 3 : v3, 4 : v4, 5 : v5}

print(find_path(graph2, 1, 3))