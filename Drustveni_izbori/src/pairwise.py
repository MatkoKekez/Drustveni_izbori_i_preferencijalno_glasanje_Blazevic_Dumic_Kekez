from itertools import permutations

def compute_pairwise(votes, candidates):
    pairwise = { (i, j): 0 for i, j in permutations(candidates, 2) }

    for ranking in votes:
        for i, j in permutations(candidates, 2):
            if ranking.index(i) < ranking.index(j):
                pairwise[(i, j)] += 1

    return pairwise


def compute_margins(pairwise, candidates):
    margins = {}

    for i, j in permutations(candidates, 2):
        margins[(i, j)] = pairwise[(i, j)] - pairwise[(j, i)]

    return margins
