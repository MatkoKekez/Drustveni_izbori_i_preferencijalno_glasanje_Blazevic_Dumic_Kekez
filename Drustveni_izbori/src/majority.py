def find_condorcet_winner(pairwise, candidates):
    for i in candidates:
        if all(pairwise[(i, j)] > pairwise[(j, i)] for j in candidates if j != i):
            return i
    return None
