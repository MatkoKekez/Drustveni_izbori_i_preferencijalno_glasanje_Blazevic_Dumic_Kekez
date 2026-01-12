# viz.py
import networkx as nx
import matplotlib.pyplot as plt

def build_majority_graph(pairwise, candidates):
    """Turnirski graf: i -> j ako i pobjeđuje j po većini."""
    G = nx.DiGraph()
    G.add_nodes_from(candidates)

    for i in candidates:
        for j in candidates:
            if i == j:
                continue
            if pairwise[(i, j)] > pairwise[(j, i)]:
                margin = pairwise[(i, j)] - pairwise[(j, i)]
                G.add_edge(i, j, label=f"{pairwise[(i,j)]}-{pairwise[(j,i)]}", margin=margin)
    return G

def draw_graph(G, title, outfile=None):
    plt.figure(figsize=(8, 6))
    pos = nx.circular_layout(G)  # čitljivo za 5 čvorova

    nx.draw_networkx_nodes(G, pos, node_size=900)
    nx.draw_networkx_labels(G, pos, font_size=12)
    nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20, width=2, min_target_margin=15)

    # label na bridovima
    edge_labels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    plt.title(title)
    plt.axis("off")

    if outfile:
        plt.tight_layout()
        plt.savefig(outfile, dpi=200)
        plt.close()
    else:
        plt.show()
