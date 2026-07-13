def movgen(node, graph):
    return graph[node]


def a_star(graph, heuristic, start, goal):
    OPEN = []
    CLOSED = []
    parent = {}
    g = {}
    f = {}

    OPEN.append(start)
    parent[start] = None
    g[start] = 0
    f[start] = g[start] + heuristic[start]

    while OPEN:
        # Select node with lowest f(n)
        current = min(OPEN, key=lambda node: f[node])
        OPEN.remove(current)

        # Goal reached
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            print("Final Path:", path)
            print("Total Cost:", g[goal])
            return path

        # Generate children
        for child, cost in movgen(current, graph):
            new_cost = g[current] + cost

            if child not in OPEN and child not in CLOSED:
                OPEN.append(child)
                parent[child] = current
                g[child] = new_cost
                f[child] = g[child] + heuristic[child]

            else:
                if g[child] > new_cost:
                    g[child] = new_cost
                    f[child] = g[child] + heuristic[child]
                    parent[child] = current

                    if child in CLOSED:
                        CLOSED.remove(child)
                        OPEN.append(child)

        print("Expanding Node:", current)
        print("g(n):", g[current], "f(n):", f[current])

        CLOSED.append(current)

        print("OPEN List:", OPEN)
        print("CLOSED List:", CLOSED)
        print("-" * 50)

    print("Goal not found:", goal)
    return None


# Graph
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 7,
    'E': 2,
    'F': 6,
    'G': 0
}

start = 'A'
goal = 'G'

a_star(graph, heuristic, start, goal)