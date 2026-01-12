from data_loader import load_votes
from pairwise import compute_pairwise
from majority import find_condorcet_winner
from ranked_pairs import ranked_pairs, ranked_pairs_winner
from schulze import schulze_method

CANDIDATES = ["A", "B", "C", "D", "E"]

def main():
    votes = load_votes("data/votes6.csv")
    pairwise = compute_pairwise(votes, CANDIDATES)

    #Većina
    print("Condorcet winner:")
    print("-->",find_condorcet_winner(pairwise, CANDIDATES))

    #Tidemanova moetoda (Ranked Pairs)
    print("\nTideman (Ranked Pairs):")
    graph = ranked_pairs(pairwise, CANDIDATES)
    print("-->Winner:", ranked_pairs_winner(graph, CANDIDATES))

    #Schulzeova metoda
    print("\nSchulze:")
    ranking, winner = schulze_method(pairwise, CANDIDATES)
    print("-->Ranking:", ranking)
    print("-->Winner:", winner)

if __name__ == "__main__":
    main()


