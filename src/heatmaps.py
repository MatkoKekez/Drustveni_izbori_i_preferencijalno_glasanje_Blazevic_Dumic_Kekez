import os
import matplotlib.pyplot as plt

def _matrix_from_dict(d, candidates, default=0):
    """Helper: dict[(i,j)] -> matrix with rows/cols in candidate order."""
    n = len(candidates)
    M = [[default for _ in range(n)] for __ in range(n)]
    for r, i in enumerate(candidates):
        for c, j in enumerate(candidates):
            if i == j:
                M[r][c] = 0
            else:
                M[r][c] = d.get((i, j), default)
    return M

def draw_pairwise_heatmap(pairwise, candidates, title, outfile):
    """
    Heatmap of pairwise margins: margin(i,j) = pairwise(i,j) - pairwise(j,i).
    Positive means i beats j; negative means i loses to j.
    """
    margins = {}
    for i in candidates:
        for j in candidates:
            if i == j:
                continue
            margins[(i, j)] = pairwise[(i, j)] - pairwise[(j, i)]

    M = _matrix_from_dict(margins, candidates, default=0)

    plt.figure(figsize=(7, 6))
    im = plt.imshow(M)  
    plt.colorbar(im)

    plt.xticks(range(len(candidates)), candidates)
    plt.yticks(range(len(candidates)), candidates)

    for r in range(len(candidates)):
        for c in range(len(candidates)):
            plt.text(c, r, str(M[r][c]), ha="center", va="center", fontsize=10)

    plt.title(title)
    plt.tight_layout()

    os.makedirs(os.path.dirname(outfile), exist_ok=True)
    plt.savefig(outfile, dpi=200)
    plt.close()

def draw_schulze_heatmap(p, candidates, title, outfile):
    """
    Heatmap of Schulze strongest paths p(i,j).
    Higher means stronger beatpath from i to j.
    """
    M = _matrix_from_dict(p, candidates, default=0)

    plt.figure(figsize=(7, 6))
    im = plt.imshow(M) 
    plt.colorbar(im)

    plt.xticks(range(len(candidates)), candidates)
    plt.yticks(range(len(candidates)), candidates)

    for r in range(len(candidates)):
        for c in range(len(candidates)):
            plt.text(c, r, str(M[r][c]), ha="center", va="center", fontsize=10)

    plt.title(title)
    plt.tight_layout()

    os.makedirs(os.path.dirname(outfile), exist_ok=True)
    plt.savefig(outfile, dpi=200)
    plt.close()
