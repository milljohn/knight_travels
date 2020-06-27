# Inner edges of the board, 2 in

def innerEdges(n=8):
    edges = []

    for i in range(1, n + 1):
        edges.append(i)
        edges.append(i + n)

    for i in range(n * n - n + 1, n * n + 1):
        edges.append(i)
        # edges.append(i - n)

    for i in range(2, n):
        edges.append((i - 1) * n + 1)
        edges.append((i - 1) * n + 2)
        edges.append(i * n - 1)
        edges.append(i * n)
    return sorted(edges)
