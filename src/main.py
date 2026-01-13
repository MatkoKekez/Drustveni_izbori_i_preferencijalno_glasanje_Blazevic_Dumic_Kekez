from data_loader import load_votes
from pairwise import compute_pairwise
from majority import find_condorcet_winner
from ranked_pairs import ranked_pairs, ranked_pairs_winner
from schulze import schulze_method

import os
import networkx as nx

from viz import build_majority_graph, build_schulze_graph, draw_graph
from heatmaps import draw_pairwise_heatmap, draw_schulze_heatmap
from matrix import save_matrix_txt


CANDIDATES = ["A", "B", "C", "D", "E"]

FILES = [
    "data/votes4.csv",
    "data/votes5.csv",
    "data/votes6.csv",
]

RESULTS_DIR = "results"


def ensure_dirs(base_dir):
    paths = [
        f"{base_dir}/pairwise/grafovi",
        f"{base_dir}/pairwise/heatmape",
        f"{base_dir}/pairwise/matrice",

        f"{base_dir}/schulze/grafovi",
        f"{base_dir}/schulze/heatmape",
        f"{base_dir}/schulze/matrice",

        f"{base_dir}/ranked_pairs/grafovi",
    ]
    for p in paths:
        os.makedirs(p, exist_ok=True)


def print_matrix_from_dict(d, candidates, name):
    print(f"\n{name}:")
    print("    " + "  ".join(candidates))
    for i in candidates:
        row = []
        for j in candidates:
            if i == j:
                row.append("0")
            else:
                row.append(str(d.get((i, j), 0)))
        print(f"{i}: " + "  ".join(row))


def validate_file(path: str):
    print("=" * 60)
    print("FILE:", path)
    print("Saved results to:", RESULTS_DIR)

    votes = load_votes(path)
    print("Loaded votes:", len(votes))

    pairwise = compute_pairwise(votes, CANDIDATES)

    cw = find_condorcet_winner(pairwise, CANDIDATES)
    print("Condorcet winner:", cw)

    rp_graph = ranked_pairs(pairwise, CANDIDATES)
    rp_winner = ranked_pairs_winner(rp_graph, CANDIDATES)
    print("Ranked Pairs winner:", rp_winner)

    schulze_ranking, schulze_winner, p = schulze_method(pairwise, CANDIDATES)
    print("Schulze winner:", schulze_winner)
    print("Schulze ranking:", schulze_ranking)

    print_matrix_from_dict(pairwise, CANDIDATES, "PAIRWISE V(i,j)")
    print_matrix_from_dict(p, CANDIDATES, "SCHULZE p(i,j)")

    base = os.path.splitext(os.path.basename(path))[0]

    majG = build_majority_graph(pairwise, CANDIDATES)
    draw_graph(
        majG,
        title=f"Majority graf ({base})",
        outfile=f"{RESULTS_DIR}/pairwise/grafovi/majority_{base}.png"
    )

    dag = nx.DiGraph()
    dag.add_nodes_from(CANDIDATES)
    for u in rp_graph:
        for v in rp_graph[u]:
            dag.add_edge(u, v, label="")
    draw_graph(
        dag,
        title=f"Ranked Pairs DAG ({base})",
        outfile=f"{RESULTS_DIR}/ranked_pairs/grafovi/rankedpairs_{base}.png"
    )

    schG = build_schulze_graph(p, CANDIDATES)
    draw_graph(
        schG,
        title=f"Schulze graf (beatpaths) ({base})",
        outfile=f"{RESULTS_DIR}/schulze/grafovi/schulze_{base}.png"
    )

    draw_pairwise_heatmap(
        pairwise,
        CANDIDATES,
        title=f"Pairwise margine ({base})",
        outfile=f"{RESULTS_DIR}/pairwise/heatmape/heatmap_pairwise_{base}.png"
    )

    draw_schulze_heatmap(
        p,
        CANDIDATES,
        title=f"Schulze p(i,j) ({base})",
        outfile=f"{RESULTS_DIR}/schulze/heatmape/heatmap_schulze_{base}.png"
    )

    save_matrix_txt(
        pairwise,
        CANDIDATES,
        f"{RESULTS_DIR}/pairwise/matrice/pairwise_{base}.txt",
        name=f"PAIRWISE V(i,j) ({base})"
    )

    save_matrix_txt(
        p,
        CANDIDATES,
        f"{RESULTS_DIR}/schulze/matrice/schulze_p_{base}.txt",
        name=f"SCHULZE p(i,j) ({base})"
    )
    print(f"Done. Generated files for {base} in {RESULTS_DIR}\n")


def main():
    ensure_dirs(RESULTS_DIR)
    for f in FILES:
        validate_file(f)


if __name__ == "__main__":
    main()
