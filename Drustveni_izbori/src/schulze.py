from itertools import permutations

def schulze_method(pairwise, candidates):
    p = { (i, j): 0 for i, j in permutations(candidates, 2) }

    for i, j in permutations(candidates, 2):
        if pairwise[(i, j)] > pairwise[(j, i)]:
            p[(i, j)] = pairwise[(i, j)]

    for i in candidates:
        for j in candidates:
            if i == j:
                continue
            for k in candidates:
                if i == k or j == k:
                    continue
                p[(j, k)] = max(
                    p[(j, k)],
                    min(p[(j, i)], p[(i, k)])
                )

    def beats(i, j):
        return p[(i, j)] > p[(j, i)]

    ranking = sorted(
        candidates,
        key=lambda x: sum(beats(x, y) for y in candidates if y != x),
        reverse=True
    )

    return ranking, ranking[0]
