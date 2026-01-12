from data_loader import load_votes
from pairwise import compute_pairwise
from majority import find_condorcet_winner
from ranked_pairs import ranked_pairs, ranked_pairs_winner
from schulze import schulze_method
import os
import networkx as nx

from viz import build_majority_graph, draw_graph

CANDIDATES = ["A", "B", "C", "D", "E"]

FILES = [
    "data/votes4.csv",
    "data/votes5.csv",
    "data/votes6.csv",
]

def validate_file(path: str):
    print("=" * 60)
    print("FILE:", path)

    votes = load_votes(path)
    print("Loaded votes:", len(votes))

    pairwise = compute_pairwise(votes, CANDIDATES)

    cw = find_condorcet_winner(pairwise, CANDIDATES)
    print("Condorcet winner:", cw)

    rp_graph = ranked_pairs(pairwise, CANDIDATES)
    rp_winner = ranked_pairs_winner(rp_graph, CANDIDATES)
    print("Ranked Pairs winner:", rp_winner)

    schulze_ranking, schulze_winner = schulze_method(pairwise, CANDIDATES)
    print("Schulze winner:", schulze_winner)
    print("Schulze ranking:", schulze_ranking)

    # =========================
    # VIZUALIZACIJA
    # =========================

    # gdje spremamo slike
    os.makedirs("results", exist_ok=True)

    # ime bez .csv (npr. votes4)
    base = os.path.splitext(os.path.basename(path))[0]

    # (1) Majority graf iz pairwise matrice
    majG = build_majority_graph(pairwise, CANDIDATES)
    draw_graph(
        majG,
        title=f"Majority graf ({base})",
        outfile=f"results/majority_{base}.png"
    )

    # (2) Ranked Pairs DAG (iz rp_graph dict-a)
    DAG = nx.DiGraph()
    DAG.add_nodes_from(CANDIDATES)
    for u in rp_graph:
        for v in rp_graph[u]:
            DAG.add_edge(u, v)

    draw_graph(
        DAG,
        title=f"Ranked Pairs DAG ({base})",
        outfile=f"results/rankedpairs_{base}.png"
    )

def main():
    for f in FILES:
        validate_file(f)

if __name__ == "__main__":
    main()
