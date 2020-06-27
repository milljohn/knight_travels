def boardEdges(n=8):
    edges = []

    for i in range(1, n + 1):
        edges.append(i)

    for i in range(n * n - n + 1, n * n + 1):
        edges.append(i)

    for i in range(2, n):
        edges.append((i - 1) * n + 1)
        edges.append(i * n)

    return edges.sort()
