import csv

CANDIDATES = ["A", "B", "C", "D", "E"]

def load_votes(filepath):
    votes = []

    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ranking = [
                row["rank_1"],
                row["rank_2"],
                row["rank_3"],
                row["rank_4"],
                row["rank_5"],
            ]

            if set(ranking) != set(CANDIDATES):
                raise ValueError("Incorrect vote: not a complete order!")

            votes.append(ranking)

    return votes
