from itertools import permutations

def creates_cycle(graph, start, end):
    stack = [end]
    visited = set()

    while stack:
        node = stack.pop()
        if node == start:
            return True
        if node not in visited:
            visited.add(node)
            stack.extend(graph.get(node, []))

    return False


def ranked_pairs(pairwise, candidates):
    edges = []

    for i, j in permutations(candidates, 2):
        if pairwise[(i, j)] > pairwise[(j, i)]:
            strength = pairwise[(i, j)] - pairwise[(j, i)]
            edges.append((i, j, strength))

    edges.sort(key=lambda x: -x[2])

    graph = {c: [] for c in candidates}

    for winner, loser, _ in edges:
        if not creates_cycle(graph, winner, loser):
            graph[winner].append(loser)

    return graph


def ranked_pairs_winner(graph, candidates):
    for c in candidates:
        if all(c not in graph[other] for other in candidates):
            return c
    return None
